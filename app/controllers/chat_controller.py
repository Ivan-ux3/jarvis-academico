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


def executar_tool(tool_name, arguments):

    tool_function = TOOLS.get(tool_name)

    if not tool_function:
        return f"Ferramenta '{tool_name}' não encontrada."

    try:
        return tool_function(**arguments)

    except Exception as e:
        return f"[ERRO TOOL CALLING] {str(e)}"


def processar_mensagem(mensagem):

    resposta_llm = perguntar_llm(mensagem)

    try:

        tool_call = json.loads(resposta_llm)

        tool_name = tool_call.get("tool")

        arguments = tool_call.get("arguments", {})

        resultado_tool = executar_tool(
            tool_name,
            arguments
        )

        prompt_final = f"""
O usuário perguntou:
{mensagem}

Resultado da ferramenta:
{resultado_tool}

Agora responda ao usuário de forma natural, amigável e útil.

NÃO mostre JSON.
NÃO explique ferramentas internas.
"""

        resposta_final = perguntar_llm(prompt_final)

        return resposta_final

    except json.JSONDecodeError:

        return resposta_llm