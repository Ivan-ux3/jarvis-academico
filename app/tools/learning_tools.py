from app.rag.retrieval import buscar_documentos

from app.learning.active_recall import (
    gerar_pergunta
)

from app.services.logging_service import registrar_log


def gerar_pergunta_estudo(topico):

    documentos = buscar_documentos(topico)

    contexto = '\n'.join(documentos)

    pergunta = gerar_pergunta(contexto)

    registrar_log(
        'gerar_pergunta_estudo',
        topico,
        pergunta
    )

    return pergunta