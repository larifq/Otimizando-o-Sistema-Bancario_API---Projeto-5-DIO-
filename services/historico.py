from models.historico import Historico
from models.conta import Conta
from models.conta_corrente import ContaCorrente
from schemas.historico import SchemaHistorico, SchemaTransacao
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from datetime import datetime, date

async def registrar_historico(sessao: AsyncSession, transacao: SchemaTransacao, id_conta: int, tipo_transacao: str, tipo_conta: str):
        insert_historico = Historico(
            valor = transacao.valor,
            tipo_transacao = tipo_transacao,
            tipo_conta = tipo_conta,
            data_transacao = datetime.now(),
            id_conta = id_conta)
            
        sessao.add(insert_historico)

        await sessao.commit()
        await sessao.refresh(insert_historico)
        return {"valor": insert_historico.valor, "data_transacao": insert_historico.data_transacao, "saldo_atual": insert_historico.conta.saldo}

async def registrar_deposito_service(sessao: AsyncSession, transacao: SchemaTransacao, id_conta: int):
    conta = await sessao.get(Conta, id_conta)

    if not conta:
        raise ValueError("Conta inexistente!")
    
    id_conta = conta.id

    if transacao.valor <= 0:
        raise ValueError("Operação falhou! Verifique se o valor informado é válido.")
   
    conta.saldo += transacao.valor
   
    sessao.add(conta)

    return await registrar_historico(sessao, transacao, id_conta, tipo_transacao = "Deposito", tipo_conta = "Conta Corrente")


async def registrar_saque_service(sessao: AsyncSession, transacao: SchemaTransacao, id_conta: int):
    conta = await sessao.get(Conta, id_conta)

    if not conta:
        raise "Conta inexistente!"
    
    data_atual = date.today()
    select_conta_corrente = await sessao.execute(select(ContaCorrente).where(ContaCorrente.id_conta == conta.id))
    conta_corrente = select_conta_corrente.scalars().first()
    limite = conta_corrente.limite
    limite_saque = conta_corrente.limite_saque
    select_numero_saque = await sessao.execute(select(func.count(Historico.tipo_transacao == "Saque")).where(Historico.id_conta == id_conta, func.date(Historico.data_transacao) == data_atual))
    numero_saque = select_numero_saque.scalars().first()

    if conta.saldo > transacao.valor:
        if transacao.valor > limite:
            print("Operação falhou! Ultrapassou o valor de limite diário de saque, tente novamente outro dia.")

        elif limite_saque > numero_saque:
            print("Operação falhou! Ultrapassou a quantidade de saque diária, tente novamente outro dia.")

        else:
            conta.saldo -= transacao.valor
            sessao.add(conta)
            
            return await registrar_historico(sessao, transacao, id_conta, tipo_transacao = "Saque", tipo_conta = "Conta Corrente")
        
        raise "Saldo insuficiente!"


async def buscar_historicos_service(sessao: AsyncSession, id_conta: int):
    conta = await sessao.get(Conta, id_conta)

    if not conta:
        raise ValueError("Conta inexistente!")
                                  
    select_historicos = await sessao.execute(select(Historico).where(Historico.id_conta == conta.id))
    resultado = select_historicos.scalars().all()
    return  resultado

async def buscar_saques_service(sessao: AsyncSession, id_conta: int):
    conta = await sessao.get(Conta, id_conta)

    if not conta:
        raise ValueError("Conta inexistente!")
                                  
    select_historicos = await sessao.execute(select(Historico).where(Historico.id_conta == conta.id, Historico.tipo_transacao == "Saque"))
    resultado = select_historicos.scalars().all()
    return resultado

async def buscar_depositos_service(sessao: AsyncSession, id_conta: int):
    conta = await sessao.get(Conta, id_conta)

    if not conta:
        raise ValueError("Conta inexistente!")
                                  
    select_historicos = await sessao.execute(select(Historico).where(Historico.id_conta == conta.id, Historico.tipo_transacao == "Deposito"))
    resultado = select_historicos.scalars().all()
    return  resultado

