from app.rag.retrieval import buscar_documentos
from app.services.logging_service import registrar_log
from app.services.llm_service import client


def buscar_material_rag(query):

    if not query:
        return "Nenhuma pergunta enviada."

    documentos = buscar_documentos(query)

    registrar_log(
        'buscar_material_rag',
        query,
        f'{len(documentos)} documentos recuperados'
    )

    if not documentos:
        return "Nenhum documento encontrado."

    # proteção para testes sem API
    if client is None:
        return "LLM não configurada."

    contexto = "\n".join(documentos)

    prompt = f"""
Você é um assistente acadêmico.

Explique de forma clara e didática.

Use APENAS o contexto abaixo:

{contexto}

Pergunta:
{query}
"""

    resposta = client.chat.completions.create(
        model="google/gemma-3-12b-it",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta.choices[0].message.content
