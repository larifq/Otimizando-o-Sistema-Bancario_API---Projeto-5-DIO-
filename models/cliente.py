from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

from db.setup import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_endereco = Column(Integer, ForeignKey("endereco.id"), nullable=False, unique=True)
    

    conta = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")
    pessoa_fisica = relationship("PessoaFisica", back_populates="cliente", cascade="all, delete-orphan", single_parent=True, uselist=False)
    endereco = relationship("Endereco", back_populates="cliente", cascade="all, delete-orphan", single_parent=True, uselist=False)