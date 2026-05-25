from app.rag.retrieval import buscar_documentos

from app.services.logging_service import registrar_log


def buscar_material_rag(pergunta):

    documentos = buscar_documentos(pergunta)

    registrar_log(
        'buscar_material_rag',
        pergunta,
        f'{len(documentos)} documentos recuperados'
    )

    contexto = '\n'.join(documentos)

    return contexto