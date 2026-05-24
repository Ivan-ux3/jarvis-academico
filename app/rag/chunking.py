def chunk_text(texto, chunk_size=500, overlap=100):

    chunks = []

    inicio = 0

    while inicio < len(texto):

        fim = inicio + chunk_size

        chunk = texto[inicio:fim]

        chunks.append(chunk)

        inicio += chunk_size - overlap

    return chunks