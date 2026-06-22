<<<<<<< HEAD
from app.controllers.study_controller import StudyController
from app.services.logging_service import registrar_log

controller = StudyController()


def consultar_contexto_estudos(tema=None):

    contexto = controller.obter_contexto_estudos(tema)

    registrar_log(
        "consultar_contexto_estudos",
        tema,
        "contexto gerado"
    )

    return contexto


def planejar_estudos(tema=None):

    plano_estudos = controller.gerar_plano_estudos(tema)

    registrar_log(
        "planejar_estudos",
        tema,
        "plano de estudos gerado"
    )

    return plano_estudos
=======
from app.tools.agenda_tools import consultar_agenda
from app.tools.task_tools import tool_listar_tarefas
from app.rag.retrieval import buscar_documentos

from app.services.logging_service import registrar_log


def gerar_plano_estudos(topico="redes"):

    try:

        agenda = consultar_agenda()

        tarefas = tool_listar_tarefas()

        materiais = buscar_documentos(topico)

        plano = []

        if agenda == 'Nenhum evento encontrado.':
            plano.append(
                'Nenhuma prova agendada encontrada.'
            )

        else:
            plano.append(
                'Verifique eventos próximos da agenda.'
            )


        if tarefas == 'Nenhuma tarefa encontrada.':
            plano.append(
                'Nenhuma tarefa pendente.'
            )

        else:
            plano.append(
                'Priorize tarefas pendentes.'
            )


        if materiais:

            plano.append(
                f'Estude materiais sobre {topico}.'
            )

        else:

            plano.append(
                'Nenhum material encontrado.'
            )


        resultado = '\n'.join(plano)


        registrar_log(

            'gerar_plano_estudos',

            {
                'agenda': agenda,
                'tarefas': tarefas,
                'topico': topico
            },

            resultado

        )

        return resultado


    except Exception as erro:


        registrar_log(

            'gerar_plano_estudos',

            topico,

            str(erro)

        )


        return f'Erro ao gerar plano: {erro}'
>>>>>>> main
