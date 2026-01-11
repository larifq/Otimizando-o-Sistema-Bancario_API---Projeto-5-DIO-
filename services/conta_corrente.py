from models.conta import Conta
from models.login import Login
from models.conta_corrente import ContaCorrente
from schemas.conta_corrente import SchemaContaCorrente, SchemaContaCorrenteUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from fastapi import HTTPException


async def criar_conta_corrente_service(sessao: AsyncSession, conta_corrente: SchemaContaCorrente):
     
     insert_conta_corrente = ContaCorrente(
          limite = conta_corrente.limite,
          conta = Conta(
          saldo = conta_corrente.conta.saldo,
          agencia = conta_corrente.conta.agencia,
          id_cliente = conta_corrente.conta.id_cliente, 
          login = Login(
          senha = conta_corrente.conta.login.senha)))


     sessao.add(insert_conta_corrente)

     await sessao.commit()
     await sessao.refresh(insert_conta_corrente)
     return insert_conta_corrente

async def buscar_contas_corrente_service(sessao: AsyncSession):
        select_contas_corrente = await sessao.execute(select(ContaCorrente))
        resultado = select_contas_corrente.scalars().all()
        return  resultado


async def buscar_conta_corrente_service(sessao: AsyncSession, id = int):
        select_conta_corrente = await sessao.execute(select(ContaCorrente).where(ContaCorrente.id == id))
        resultado = select_conta_corrente.scalars().all()
        return  resultado


async def atualizar_conta_corrente_service(conta_corrente: ContaCorrente, sessao: AsyncSession, id = int):
     informacao_conta_corrente_antes = await sessao.get(ContaCorrente, id)

     if not informacao_conta_corrente_antes:
               raise "Conta inexistente!"
     schema_conta_corrente = conta_corrente.model_dump(exclude_unset=True)
     update_conta_corrente = update(ContaCorrente).where(ContaCorrente.id == id).values(**schema_conta_corrente)

     await sessao.execute(update_conta_corrente)
     await sessao.commit()
     informacao_conta_corrente_depois = await sessao.get(ContaCorrente, id)
     await sessao.refresh(informacao_conta_corrente_depois)
     return [informacao_conta_corrente_depois]