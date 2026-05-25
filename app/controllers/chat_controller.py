import json

from app.services.llm_service import perguntar_llm

from app.tools.task_tools import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa
)

from app.tools.agenda_tools import (
    adicionar_evento_agenda,
    consultar_agenda
)

from app.tools.rag_tools import buscar_material_rag

from app.tools.learning_tools import (
    gerar_pergunta_estudo
)


TOOLS = {
    "adicionar_tarefa": adicionar_tarefa,
    "listar_tarefas": listar_tarefas,
    "concluir_tarefa": concluir_tarefa,
    "adicionar_evento_agenda": adicionar_evento_agenda,
    "consultar_agenda": consultar_agenda,
    "buscar_material_rag": buscar_material_rag,
    "gerar_pergunta_estudo": gerar_pergunta_estudo,
}


SYSTEM_PROMPT = """
Você é o JARVIS Acadêmico, um assistente inteligente para estudantes.

Você possui acesso às seguintes ferramentas:

1. adicionar_tarefa
- adiciona uma tarefa
- argumento esperado:
{
  "tarefa": "texto"
}

2. listar_tarefas
- lista tarefas cadastradas
- sem argumentos

3. concluir_tarefa
- conclui uma tarefa
- argumento esperado:
{
  "id": numero
}

4. adicionar_evento_agenda
- adiciona um evento na agenda
- argumentos esperados:
{
  "titulo": "texto",
  "data": "YYYY-MM-DD"
}

5. consultar_agenda
- consulta eventos da agenda
- sem argumentos

6. buscar_material_rag
- busca conteúdo nos PDFs
- argumento esperado:
{
  "query": "texto"
}

7. gerar_pergunta_estudo
- gera perguntas de estudo
- argumento esperado:
{
  "topico": "texto"
}

REGRAS IMPORTANTES:
- Quando precisar usar uma ferramenta, responda APENAS com JSON válido.
- Nunca coloque explicações antes ou depois do JSON.
- Quando NÃO precisar de ferramenta, responda normalmente.
- Nunca invente ferramentas.
"""


def executar_tool(tool_name, arguments):

    tool_function = TOOLS.get(tool_name)

    if not tool_function:
        return f"Ferramenta '{tool_name}' não encontrada."

    try:
        return tool_function(**arguments)

    except Exception as e:
        return f"[ERRO TOOL CALLING] {str(e)}"


def processar_mensagem(mensagem):

    resposta_llm = perguntar_llm(
        mensagem_usuario=mensagem,
        system_prompt=SYSTEM_PROMPT
    )

    try:

        tool_call = json.loads(resposta_llm)

        tool_name = tool_call.get("tool")

        arguments = tool_call.get("arguments", {})

        resultado_tool = executar_tool(
            tool_name,
            arguments
        )

        prompt_final = f"""
O usuário enviou a seguinte mensagem:

{mensagem}

Uma ferramenta foi utilizada.

Ferramenta:
{tool_name}

Resultado da ferramenta:
{resultado_tool}

Agora responda ao usuário de forma natural, amigável e útil.

NÃO mostre JSON.
NÃO explique ferramentas internas.
"""

        resposta_final = perguntar_llm(
            mensagem_usuario=prompt_final
        )

        return resposta_final

    except json.JSONDecodeError:

        return resposta_llm