import os

from pypdf import PdfReader

from app.rag.chunking import chunk_text


def carregar_pdf(caminho_pdf):

    reader = PdfReader(caminho_pdf)

    texto = ''

    for page in reader.pages:
        texto += page.extract_text()

    return texto


def processar_documentos():

    pasta = 'data/documentos/pdfs'

    documentos = []

    for arquivo in os.listdir(pasta):

        if arquivo.endswith('.pdf'):

            caminho = os.path.join(pasta, arquivo)

            texto = carregar_pdf(caminho)

            chunks = chunk_text(texto)

            documentos.append({
                'arquivo': arquivo,
                'chunks': chunks
            })

    return documentos