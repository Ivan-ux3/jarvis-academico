import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
MODEL_NAME = os.getenv('MODEL_NAME')

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

TOOLS = [
    {
        'name': 'listar_tarefas',
        'description': 'Lista tarefas do usuário'
    },
    {
        'name': 'adicionar_tarefa',
        'description': 'Adiciona uma nova tarefa'
    },
    {
        'name': 'concluir_tarefa',
        'description': 'Conclui uma tarefa'
    },
    {
        'name': 'consultar_agenda',
        'description': 'Consulta agenda acadêmica'
    },
    {
        'name': 'adicionar_evento_agenda',
        'description': 'Adiciona evento na agenda acadêmica'
    },
    {
        'name': 'buscar_material_rag',
        'description': 'Busca informações nos materiais de estudo'
    },
    {
        'name': 'gerar_pergunta_estudo',
        'description': 'Gera pergunta de estudo para active recall'
    }
]


def perguntar_llm(mensagem):

    prompt = f'''
Você é o JARVIS Acadêmico.

Você possui acesso às seguintes ferramentas:

{json.dumps(TOOLS, indent=2, ensure_ascii=False)}

REGRAS OBRIGATÓRIAS:

- Se precisar usar ferramenta, responda SOMENTE JSON.
- NÃO escreva explicações antes do JSON.
- NÃO escreva explicações depois do JSON.
- NÃO converse junto com JSON.
- Sua resposta deve conter APENAS o JSON puro.
- Nunca use markdown.
- Nunca use ```json.

EXEMPLO CORRETO:
{{
    "tool": "buscar_material_rag",
    "arguments": {{
        "query": "TCP"
    }}
}}

Use buscar_material_rag quando:
- o usuário pedir explicações
- o usuário quiser aprender conteúdo
- o usuário perguntar sobre redes
- o usuário pedir conceitos acadêmicos

Use gerar_pergunta_estudo quando:
- o usuário pedir quiz
- o usuário pedir perguntas
- o usuário quiser praticar
- o usuário quiser active recall

Se NÃO precisar usar ferramenta:
- responda normalmente em texto natural.

Mensagem do usuário:
{mensagem}
'''

    resposta = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return resposta.choices[0].message.content