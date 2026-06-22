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

    if not tema:
        tema = "Redes"

    plano_estudos = controller.gerar_plano_estudos(tema)

    registrar_log(
        "planejar_estudos",
        tema,
        "plano de estudos gerado"
    )

    return plano_estudos
