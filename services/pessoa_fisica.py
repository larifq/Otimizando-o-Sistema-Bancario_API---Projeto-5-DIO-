from models.pessoa_fisica import PessoaFisica
from schemas.pessoa_fisica import SchemaPessoaFisicaUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update



async def buscar_pessoa_fisica_service(sessao: AsyncSession):
        select_endereco = await sessao.execute(select(PessoaFisica))
        resultado = select_endereco.scalars().all()
        return  resultado

async def buscar_pessoas_fisica_service(sessao: AsyncSession, id = int):
        select_endereco = await sessao.execute(select(PessoaFisica).where(PessoaFisica.id == id))
        resultado = select_endereco.scalars().all()
        return  resultado

async def atualizar_pessoas_fisica_service(schema_pessoa_fisica: SchemaPessoaFisicaUpdate,sessao: AsyncSession, id = int):
     
     dados_pessoa_fisica_antes = await sessao.get(PessoaFisica, id)
     
     if not dados_pessoa_fisica_antes:
           raise "Dado inexistente!"
     
     schema_pessoa_fisica = schema_pessoa_fisica.model_dump(exclude_unset=True)
     update_pessoa_fisica = update(PessoaFisica).where(PessoaFisica.id == id).values(**schema_pessoa_fisica)
     await sessao.execute(update_pessoa_fisica)
     await sessao.commit()
     dados_pessoa_fisica_depois = await sessao.get(PessoaFisica, id)
     return [dados_pessoa_fisica_depois]