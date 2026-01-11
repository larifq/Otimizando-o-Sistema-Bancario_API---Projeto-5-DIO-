from models.endereco import Endereco
from schemas.endereco import SchemaEnderecoUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update


async def buscar_enderecos_service(sessao: AsyncSession):
        select_enderecos = await sessao.execute(select(Endereco))
        resultado = select_enderecos.scalars().all()
        return  resultado


async def buscar_endereco_service(sessao: AsyncSession, id = int):
        select_endereco = await sessao.execute(select(Endereco).where(Endereco.id == id))
        resultado = select_endereco.scalars().all()
        return  resultado

async def atualizar_endereco_service(schema_endereco: SchemaEnderecoUpdate,sessao: AsyncSession, id = int):
     
        endereco_cliente_antes = await sessao.get(Endereco, id)
     
        if not endereco_cliente_antes:
                raise "Endereço inexistente!"
        
        schema_endereco = schema_endereco.model_dump(exclude_unset=True)
        update_endereco = update(Endereco).where(Endereco.id == id).values(**schema_endereco)
        await sessao.execute(update_endereco)
        await sessao.commit()
        endereco_cliente_depois = await sessao.get(Endereco, id)
        await sessao.refresh(endereco_cliente_depois)
        return [endereco_cliente_depois]
