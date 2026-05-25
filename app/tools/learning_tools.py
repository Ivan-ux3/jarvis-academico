from app.rag.retrieval import buscar_documentos

from app.learning.active_recall import gerar_pergunta

from app.services.logging_service import registrar_log


def gerar_pergunta_estudo(topico=None, **kwargs):

    # normalização de entrada (LLM pode variar nomes)
    if not topico:
        topico = (
            kwargs.get("topic")
            or kwargs.get("topico")
            or kwargs.get("query")
            or kwargs.get("tema")
            or kwargs.get("assunto")
            or kwargs.get("texto")
        )

    if not topico:
        return "[ERRO] tópico não informado."

    documentos = buscar_documentos(topico)

    if not documentos:
        return "Nenhum conteúdo encontrado para esse tópico."

    contexto = "\n".join(documentos)

    pergunta = gerar_pergunta(contexto)

    registrar_log(
        'gerar_pergunta_estudo',
        topico,
        pergunta
    )

    return pergunta