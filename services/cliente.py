from models.cliente import Cliente
from models.endereco import Endereco
from models.pessoa_fisica import PessoaFisica
from schemas.cliente import SchemaCliente
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload, joinedload


async def criar_cliente_service(sessao: AsyncSession, cliente: SchemaCliente):

     insert_cliente = Cliente(endereco = Endereco(**cliente.endereco.model_dump()),
          pessoa_fisica = PessoaFisica(
          cpf = cliente.pessoa_fisica.cpf,
          nome = cliente.pessoa_fisica.nome,
          data_nascimento = cliente.pessoa_fisica.data_nascimento))
     
     sessao.add(insert_cliente)


     await sessao.commit()
     await sessao.refresh(insert_cliente)
     return insert_cliente


async def buscar_clientes_service(sessao: AsyncSession):
                              
     select_clientes = await sessao.execute(select(Cliente))
     resultado = select_clientes.scalars().all()
     
     return resultado

async def buscar_cliente_service(sessao: AsyncSession, id = int):

     select_cliente = select(Cliente).where(Cliente.id == id)
     realizar_select = await sessao.execute(select_cliente)
     resultado = realizar_select.scalars().all()
     return resultado

async def deletar_cliente_service(sessao: AsyncSession, id = int):
     deletar_cliente = delete(Cliente).where(Cliente.id == id)     
     resultado = await sessao.execute(deletar_cliente)
     await sessao.commit()
     return resultado
