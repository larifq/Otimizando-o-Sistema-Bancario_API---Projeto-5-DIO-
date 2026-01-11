from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models.cliente import Cliente
from models.conta import Conta
from models.conta_corrente import ContaCorrente
from models.endereco import Endereco
from models.historico import Historico
from models.login import Login
from models.pessoa_fisica import PessoaFisica


engine = create_async_engine("sqlite+aiosqlite:///sistema_bancario.db")

sessao_assincrona = sessionmaker(
    engine,
    class_= AsyncSession,
    expire_on_commit = False
)

async def session():
    async with sessao_assincrona() as sessao:
        yield sessao