from models.conta import Conta
from schemas.conta import SchemaConta, SchemaContaUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete


async def buscar_contas_service(sessao: AsyncSession):
        select_contas = await sessao.execute(select(Conta))
        resultado = select_contas.scalars().all()
        return  resultado


async def buscar_conta_service(sessao: AsyncSession, id = int):
        select_conta = await sessao.execute(select(Conta).where(Conta.id == id))
        resultado = select_conta.scalars().all()
        return  resultado


async def atualizar_conta_service(conta: SchemaContaUpdate, sessao: AsyncSession, id = int):
     informacao_conta_antes = await sessao.get(Conta, id)

     if not informacao_conta_antes:
               raise "Conta inexistente!"
     
     schema_conta = conta.model_dump(exclude_unset=True)
     update_conta = update(Conta).where(Conta.id == id).values(**schema_conta)

     await sessao.execute(update_conta)
     await sessao.commit()
     informacao_conta_depois = await sessao.get(Conta, id)
     await sessao.refresh(informacao_conta_depois)
     return [informacao_conta_depois]

async def deletar_conta_service(sessao: AsyncSession, id = int):
     deletar_conta = delete(Conta).where(Conta.id == id)     
     resultado = await sessao.execute(deletar_conta)
     await sessao.commit()
     return resultado