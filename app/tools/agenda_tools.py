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


def adicionar_evento_agenda(titulo=None, data=None, tipo=None, **kwargs):

    # 🔥 normalização de argumentos (corrige erro da LLM)
    if not titulo:
        titulo = (
            kwargs.get("evento")
            or kwargs.get("nome")
            or kwargs.get("title")
        )

    if not data:
        data = (
            kwargs.get("date")
            or kwargs.get("dia")
            or kwargs.get("quando")
        )

    if not tipo:
        tipo = kwargs.get("tipo") or kwargs.get("type")

        if not tipo and titulo:
            titulo_lower = str(titulo).lower()

            if "prova" in titulo_lower:
                tipo = "prova"
            elif "aula" in titulo_lower:
                tipo = "aula"
            else:
                tipo = "evento"

    # 🔥 validação obrigatória
    if not titulo or not data:
        return "[ERRO] titulo ou data não informados."

    adicionar_evento(titulo, data, tipo)

    registrar_log(
        'adicionar_evento_agenda',
        titulo,
        'evento adicionado'
    )

    return 'Evento adicionado com sucesso.'