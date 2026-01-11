from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from db.setup import Base

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False, unique=True)


    cliente = relationship("Cliente", back_populates="pessoa_fisica")