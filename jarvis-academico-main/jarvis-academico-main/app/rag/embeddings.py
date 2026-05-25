from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def gerar_embedding(texto):
    return model.encode(texto).tolist()