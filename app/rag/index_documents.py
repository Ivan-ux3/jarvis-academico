from app.rag.ingest import processar_documentos
from app.rag.retrieval import salvar_chunks


def main():

    print('Processando documentos...')

    documentos = processar_documentos()

    print(f'{len(documentos)} documentos encontrados.')

    salvar_chunks(documentos)

    print('Documentos indexados com sucesso.')


if __name__ == '__main__':
    main()