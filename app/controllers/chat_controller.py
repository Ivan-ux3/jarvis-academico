import json

from app.services.llm_service import perguntar_llm, client

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


def executar_tool(tool_name, arguments):

    if tool_name == 'listar_tarefas':
        return tool_listar_tarefas()

    elif tool_name == 'adicionar_tarefa':

        descricao = (
            arguments.get('descricao')
            or arguments.get('task')
            or arguments.get('tarefa')
            or arguments.get('texto')
        )

        return tool_adicionar_tarefa(descricao)

    elif tool_name == 'concluir_tarefa':

        task_id = (
            arguments.get('task_id')
            or arguments.get('id')
        )

        return tool_concluir_tarefa(task_id)

    elif tool_name == 'consultar_agenda':
        return consultar_agenda()

    elif tool_name == 'adicionar_evento_agenda':

        titulo = (
            arguments.get('titulo')
            or arguments.get('title')
            or arguments.get('evento')
            or arguments.get('nome')
        )

        data = (
            arguments.get('data')
            or arguments.get('date')
            or arguments.get('dia')
            or arguments.get('dia_semana')
            or arguments.get('quando')
        )

        tipo = (
            arguments.get('tipo')
            or arguments.get('type')
        )

        if not tipo:

            titulo_lower = str(titulo).lower()

            if 'prova' in titulo_lower:
                tipo = 'prova'

            elif 'aula' in titulo_lower:
                tipo = 'aula'

            else:
                tipo = 'evento'

        return adicionar_evento_agenda(
            titulo,
            data,
            tipo
        )

    elif tool_name == 'buscar_material_rag':

        pergunta = (
            arguments.get('pergunta')
            or arguments.get('question')
            or arguments.get('texto')
        )

        contexto = buscar_material_rag(pergunta)

        return gerar_resposta_final(
            pergunta,
            contexto
        )

    elif tool_name == 'gerar_pergunta_estudo':

        topico = (
            arguments.get('topico')
            or arguments.get('topic')
            or arguments.get('texto')
        )

        return gerar_pergunta_estudo(topico)

    return 'Ferramenta não encontrada.'


def gerar_resposta_final(pergunta, contexto):

    prompt = f'''
Você é um assistente acadêmico.

Responda utilizando SOMENTE o contexto abaixo.

Contexto:
{contexto}

Pergunta:
{pergunta}
'''

    resposta = client.chat.completions.create(
        model='google/gemma-3-12b-it',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return resposta.choices[0].message.content


def processar_mensagem(mensagem):

    resposta_llm = perguntar_llm(mensagem)

    try:

        resposta_limpa = (
            resposta_llm
            .replace('```json', '')
            .replace('```', '')
            .strip()
        )

        resposta_json = json.loads(resposta_limpa)

        tool_name = resposta_json['tool']

        arguments = resposta_json.get('arguments', {})

        resultado_tool = executar_tool(
            tool_name,
            arguments
        )

        return resultado_tool

    except Exception as erro:

        print(f'\n[ERRO TOOL CALLING] {erro}\n')

        return resposta_llm