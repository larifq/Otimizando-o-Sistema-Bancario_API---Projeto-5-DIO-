from fastapi import APIRouter, Depends
from services.pessoa_fisica import buscar_pessoa_fisica_service, buscar_pessoas_fisica_service, atualizar_pessoas_fisica_service
from db.session import session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.pessoa_fisica import SchemaPessoaFisica, SchemaPessoaFisicaUpdate
from view.pessoa_fisica import SchemaPessoaFisicaOut
from security import valida_cliente

router = APIRouter(prefix="/pessoas_fisicas", dependencies=[Depends(valida_cliente)], tags=["pessoa fisica"])


@router.get("/")
async def buscar_pessoas_fisicas(sessao: AsyncSession = Depends(session)):
    results = await buscar_pessoa_fisica_service(sessao)
    return results


@router.get("/{id}", response_model=list[SchemaPessoaFisicaOut])
async def buscar_pessoa_fisica(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_pessoas_fisica_service(sessao, id)
    return resultado

@router.patch("/{id}", response_model=list[SchemaPessoaFisicaUpdate])
async def atualizar_pessoa_fisica(schema_endereco: SchemaPessoaFisicaUpdate, id = int, sessao: AsyncSession = Depends(session)):
    resultado = await atualizar_pessoas_fisica_service(schema_endereco, sessao, id)
    return resultado