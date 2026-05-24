from app.models.agenda_model import (
    listar_eventos,
    adicionar_evento
)

from app.services.logging_service import registrar_log


def consultar_agenda():

    eventos = listar_eventos()

    registrar_log(
        'consultar_agenda',
        'consulta agenda',
        f'{len(eventos)} eventos encontrados'
    )

    if not eventos:
        return 'Nenhum evento encontrado.'

    resposta = ''

    for evento in eventos:

        resposta += (
            f"{evento['id']} - "
            f"{evento['titulo']} | "
            f"{evento['data']} | "
            f"{evento['tipo']}\n"
        )

    return resposta


def adicionar_evento_agenda(titulo, data, tipo):

    adicionar_evento(titulo, data, tipo)

    registrar_log(
        'adicionar_evento_agenda',
        titulo,
        'evento adicionado'
    )

    return 'Evento adicionado com sucesso.'