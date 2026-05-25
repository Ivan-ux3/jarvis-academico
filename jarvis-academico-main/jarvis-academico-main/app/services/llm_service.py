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
Você é um assistente acadêmico chamado JARVIS.

Você possui ferramentas.

Ferramentas disponíveis:
{json.dumps(TOOLS, indent=2, ensure_ascii=False)}

IMPORTANTE:
- Se o usuário pedir explicações sobre conteúdo, use buscar_material_rag
- Se o usuário pedir perguntas, quiz, prática ou exercícios, use gerar_pergunta_estudo

Se precisar usar uma ferramenta, responda APENAS JSON.

Exemplo:
{{
    "tool": "nome_da_tool",
    "arguments": {{}}
}}

Caso não precise usar ferramenta, responda normalmente.

Mensagem:
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
