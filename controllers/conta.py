from fastapi import APIRouter, Depends, status
from db.session import session
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.conta import SchemaConta, SchemaContaUpdate

from services.conta import buscar_contas_service
from services.conta import buscar_conta_service
from services.conta import atualizar_conta_service
from services.conta import deletar_conta_service
from security import valida_cliente

router = APIRouter(prefix='/contas', dependencies=[Depends(valida_cliente)], tags=["conta"])


@router.get("/")
async def buscar_contas(sessao: AsyncSession = Depends(session)):
    resultado = await buscar_contas_service(sessao)
    return list(resultado)

@router.get("/{id}")
async def buscar_conta(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_conta_service(sessao, id)
    return resultado

@router.patch("/{id}")
async def atualizar_conta(schema_conta: SchemaContaUpdate, id = int, sessao: AsyncSession = Depends(session)):
    resultado = await atualizar_conta_service(schema_conta, sessao, id)
    return resultado

@router.delete("/{id}")
async def deletar_conta(sessao: AsyncSession = Depends(session), id = int):
    resultado = await deletar_conta_service(sessao, id)
    return {"msg": f"{id} deletado com sucesso!"}