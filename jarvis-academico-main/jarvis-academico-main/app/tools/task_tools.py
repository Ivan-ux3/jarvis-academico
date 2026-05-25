from app.models.task_model import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa
)

from app.services.logging_service import registrar_log


def tool_adicionar_tarefa(descricao):

    adicionar_tarefa(descricao)

    registrar_log(
        'adicionar_tarefa',
        descricao,
        'tarefa adicionada'
    )

    return 'Tarefa adicionada com sucesso.'


def tool_listar_tarefas():

    tarefas = listar_tarefas()

    registrar_log(
        'listar_tarefas',
        'consulta',
        f'{len(tarefas)} tarefas encontradas'
    )

    if not tarefas:
        return 'Nenhuma tarefa encontrada.'

    resposta = ''

    for tarefa in tarefas:
        resposta += (
            f"{tarefa['id']} - "
            f"{tarefa['descricao']} "
            f"({tarefa['status']})\n"
        )

    return resposta


def tool_concluir_tarefa(task_id):

    concluir_tarefa(task_id)

    registrar_log(
        'concluir_tarefa',
        task_id,
        'tarefa concluída'
    )

    return 'Tarefa concluída com sucesso.'