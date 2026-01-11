from fastapi import FastAPI
from controllers import clientes, endereco, pessoa_fisica, conta_corrente, conta, historico, login

tags = [{
    "name": "cliente",
    "description": "Funções relacionadas ao cliente",
},
{
    "name": "endereco",
    "description": "Funções relacionadas ao endereco do cliente",
},
{
    "name": "conta",
    "description": "Funções relacionadas a conta do cliente",
},
{
    "name": "conta corrente",
    "description": "Funções relacionadas a conta corrente referente a conta do cliente",
},
{
    "name": "historico",
    "description": "Funções relacionadas ao histórico de transações de uma conta corrente referente a conta do cliente",
},
{
    "name": "pessoa fisica",
    "description": "Funções relacionadas aos dados de pessoa física associado ao cliente",
},
{
    "name": "login",
    "description": "Realizar autenticação.",
}
]

app = FastAPI(title = "Projeto de Sistema Bancário",
    summary = "API assíncrona de sistema bancário com a finalidade de praticar o que foi aprendido nas aulas do curso de Back-end com Python da plataforma da DIO",
    description= '''
    A API contém 7 endpoint, sendo eles:

    Cliente:
        1. Criar cliente no banco de dados.
        2. Buscar todos os clientes no banco de dados.
        3. Buscar apenas um cliente no banco de dados.
        4. Deletar cliente no banco de dados.
    
    Conta Corrente:
        1. Criar uma conta corrente no banco de dados.
        2. Buscar todas as contas correntes no banco de dados.
        3. Buscar apenas uma conta corrente no banco de dados.
        4. Alterar o valor limite e/ou limite saque de um cliente no banco de dados.
    
    Conta:
        1. Buscar todas as contas no banco de dados.
        2. Buscar apenas uma conta no banco de dados.
        3. Alterar os dados da conta no banco de dados.
        4. Deletar a conta do banco de dados.

    Endereço:
        1. Buscar todos os endereços no banco de dados.
        2. Buscar apenas um endereço no banco de dados.
        3. Alterar os dados de um endereço no banco de dados.

    Histórico:
        1. Registrar deposito no banco de dados.
        2. Registrar saque no banco de dados.
        3. Buscar histórico de transações no banco de dados.
        4. Buscar saques no banco de dados.     
        5. Buscar depositos no banco de dados.   

    Pessoa Física:
        1. Buscar todos todas pessoas físicas no banco de dados.
        2. Buscar apenas uma pessoa física no banco de dados.
        3. Alterar os dados da pessoa física no banco de dados.

    Login:
        1. Realizar autenticação.
    ''',
    redoc_url=None,
    openapi_tags=tags
)
app.include_router(clientes.router)
app.include_router(endereco.router)
app.include_router(pessoa_fisica.router)
app.include_router(conta_corrente.router)
app.include_router(conta.router)
app.include_router(historico.router)
app.include_router(login.router)

