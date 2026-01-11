from fastapi import APIRouter, Depends, status
from db.session import session
from sqlalchemy.ext.asyncio import AsyncSession
from security import valida_cliente
from services.cliente import criar_cliente_service, buscar_clientes_service, buscar_cliente_service, deletar_cliente_service
from schemas.cliente import SchemaCliente
from view.cliente import SchemaClienteOut

router = APIRouter(prefix='/clientes', dependencies=[Depends(valida_cliente)], tags=["cliente"])


@router.post('/')
async def criar_cliente(cliente: SchemaCliente, sessao: AsyncSession = Depends(session)):
    resultado = await criar_cliente_service(sessao, cliente)
    return resultado


@router.get("/", response_model=list[SchemaClienteOut])
async def buscar_clientes(sessao: AsyncSession = Depends(session)):
    resultado = await buscar_clientes_service(sessao)
    return resultado

@router.get("/{id}", response_model=list[SchemaClienteOut])
async def buscar_cliente(id = int, sessao: AsyncSession = Depends(session)):
    resultado = await buscar_cliente_service(sessao, id)
    return resultado

@router.delete("/{id}")
async def deletar_cliente(sessao: AsyncSession = Depends(session), id = int):
    await deletar_cliente_service(sessao, id)
    return {"msg": f"{id} deletado com sucesso!"}
