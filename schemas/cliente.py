from pydantic import BaseModel, ConfigDict
from schemas.pessoa_fisica import SchemaPessoaFisica
from schemas.endereco import SchemaEndereco
from schemas.conta import SchemaConta
from typing import List, Optional

class SchemaCliente(BaseModel):
    endereco: SchemaEndereco
    pessoa_fisica: SchemaPessoaFisica
    conta: Optional[List[SchemaConta]] = []
    

    
