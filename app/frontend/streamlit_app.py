import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../..')
    )
)

import streamlit as st

from app.controllers.chat_controller import processar_mensagem


st.set_page_config(
    page_title='JARVIS Acadêmico',
    page_icon='🤖',
    layout='wide'
)


st.title('🤖 JARVIS Acadêmico')

st.markdown(
    '''
Assistente inteligente para estudantes.

Funcionalidades:
- RAG com PDFs
- Agenda acadêmica
- Lista de tarefas
- Active Recall
- Planejamento de estudos
'''
)


if 'historico' not in st.session_state:
    st.session_state.historico = []


with st.sidebar:

    st.header('📚 Exemplos')

    st.markdown(
        '''
### Perguntas RAG
- Explique TCP
- O que é handshake?
- Qual a diferença entre TCP e UDP?

### Agenda
- Adicionar prova de redes amanhã
- consultar agenda

### Tarefas
- adicionar tarefa estudar DNS
- listar tarefas

### Active Recall
- Me faça uma pergunta sobre TCP
'''
    )


mensagem = st.chat_input('Digite sua mensagem...')


if mensagem:

    st.session_state.historico.append(
        ('Você', mensagem)
    )

    resposta = processar_mensagem(mensagem)

    st.session_state.historico.append(
        ('JARVIS', resposta)
    )


for autor, texto in st.session_state.historico:

    with st.chat_message(autor):
        st.markdown(texto)