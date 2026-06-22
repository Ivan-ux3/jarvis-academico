import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')
MODEL_NAME = os.getenv('MODEL_NAME')


if not API_KEY or not BASE_URL or not MODEL_NAME:
    raise ValueError("Variáveis de ambiente da LLM não configuradas corretamente.")


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
    },

    {
        'name': 'gerar_plano_estudos',
        'description': 'Gera plano de estudos com base na agenda, tarefas e materiais'
    }

]


def perguntar_llm(mensagem):

    prompt = f"""
Você é um assistente acadêmico chamado JARVIS.

Você possui ferramentas disponíveis:

{json.dumps(TOOLS, indent=2, ensure_ascii=False)}

REGRAS IMPORTANTES:

- Se o usuário pedir explicações, use buscar_material_rag
- Se pedir perguntas, exercícios ou active recall, use gerar_pergunta_estudo

- Se o usuário mencionar qualquer tipo de planejamento acadêmico, use gerar_plano_estudos. Isso inclui:
  * plano de estudos
  * cronograma
  * organização de estudos
  * prioridades
  * prova próxima
  * o que estudar
  * semana de estudos

FORMATO OBRIGATÓRIO AO USAR FERRAMENTA:

Responda SOMENTE com JSON puro:

{{
    "tool": "nome_da_tool",
    "arguments": {{}}
}}

NÃO escreva texto fora do JSON.

Se não precisar de ferramenta, responda normalmente.

Mensagem:
{mensagem}
"""

    resposta = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    content = resposta.choices[0].message.content

    # tenta extrair JSON mesmo se vier sujo
    match = re.search(r"\{.*\}", content, re.DOTALL)

    return match.group(0) if match else content