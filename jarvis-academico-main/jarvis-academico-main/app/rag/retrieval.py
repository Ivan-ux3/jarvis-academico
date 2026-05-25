import chromadb

from app.rag.embeddings import gerar_embedding

client = chromadb.PersistentClient(path='data/chroma')

collection = client.get_or_create_collection('documentos')


def salvar_chunks(documentos):

    contador = 0

    for documento in documentos:

        for chunk in documento['chunks']:

            embedding = gerar_embedding(chunk)

            collection.add(
                ids=[str(contador)],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[{
                    'arquivo': documento['arquivo']
                }]
            )

            contador += 1


def buscar_documentos(pergunta, top_k=3):

    embedding = gerar_embedding(pergunta)

    resultados = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return resultados['documents'][0]