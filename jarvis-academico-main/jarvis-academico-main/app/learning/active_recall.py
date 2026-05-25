from app.services.llm_service import client
import os

MODEL_NAME = os.getenv('MODEL_NAME')


def gerar_pergunta(contexto):

    prompt = f'''
Você é um professor.

Com base no contexto abaixo, gere UMA pergunta curta
para testar o conhecimento do aluno.

Contexto:
{contexto}
'''

    resposta = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return resposta.choices[0].message.content


def avaliar_resposta(pergunta, resposta_usuario, contexto):

    prompt = f'''
Você é um professor avaliando um aluno.

Pergunta:
{pergunta}

Resposta do aluno:
{resposta_usuario}

Contexto correto:
{contexto}

Avalie:
- se está correta
- parcialmente correta
- incorreta

Explique brevemente.
'''

    resposta = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return resposta.choices[0].message.content