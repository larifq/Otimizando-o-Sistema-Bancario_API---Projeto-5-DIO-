from sqlalchemy.orm import registry

mapeamento = registry()
Base = mapeamento.generate_base()

