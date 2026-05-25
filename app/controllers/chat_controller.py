import json

from app.services.llm_service import perguntar_llm

from app.tools.task_tools import (
    tool_adicionar_tarefa,
    tool_listar_tarefas,
    tool_concluir_tarefa
)

from app.tools.agenda_tools import (
    consultar_agenda,
    adicionar_evento_agenda
)

from app.tools.rag_tools import buscar_material_rag

from app.tools.learning_tools import (
    gerar_pergunta_estudo
)


TOOLS = {
    "adicionar_tarefa": tool_adicionar_tarefa,
    "listar_tarefas": tool_listar_tarefas,
    "concluir_tarefa": tool_concluir_tarefa,
    "consultar_agenda": consultar_agenda,
    "adicionar_evento_agenda": adicionar_evento_agenda,
    "buscar_material_rag": buscar_material_rag,
    "gerar_pergunta_estudo": gerar_pergunta_estudo,
}


def executar_tool(tool_name, arguments):

    if tool_name not in TOOLS:
        return f"Ferramenta '{tool_name}' não encontrada."

    try:
        func = TOOLS[tool_name]

        if not isinstance(arguments, dict):
            arguments = {}

        print(f"[TOOL DEBUG] {tool_name} -> {arguments}")

        return func(**arguments)

    except Exception as e:
        print(f"[ERRO TOOL CALLING] {tool_name} -> {e}")
        return f"[ERRO TOOL] {str(e)}"


def processar_mensagem(mensagem):

    resposta_llm = perguntar_llm(mensagem)

    if not resposta_llm:
        return "[ERRO] LLM retornou vazio"

    resposta_limpa = (
        resposta_llm
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    print(f"[LLM RAW] {resposta_llm}")

    try:
        resposta_json = json.loads(resposta_limpa)

        tool_name = resposta_json.get("tool")
        arguments = resposta_json.get("arguments", {})

        if not tool_name:
            return resposta_llm

        print(f"[TOOL CALL] {tool_name} -> {arguments}")

        resultado_tool = executar_tool(tool_name, arguments)

        print(f"[TOOL RESULT] {resultado_tool}")

        return resultado_tool

    except json.JSONDecodeError as e:
        print(f"[JSON ERROR] {e}")
        return resposta_llm