from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.cliente import Cliente
from models.conta import Conta
from models.pessoa_fisica import PessoaFisica
from models.historico import Historico
from models.login import Login

from db.setup import Base

class Endereco(Base):
    __tablename__ = "endereco"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(50), nullable=False)
    numero = Column(String(20), nullable=False)
    bairro = Column(String(50), nullable=False)
    cidade = Column(String(50), nullable=False)
    uf = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)

    cliente = relationship("Cliente", back_populates="endereco", uselist=False)