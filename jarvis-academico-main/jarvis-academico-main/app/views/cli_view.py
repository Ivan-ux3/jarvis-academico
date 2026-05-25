from app.controllers.chat_controller import processar_mensagem


def iniciar_chat():

    print('\nJARVIS Acadêmico iniciado.\n')

    while True:

        mensagem = input('Você: ')

        if mensagem.lower() == 'sair':
            break

        resposta = processar_mensagem(mensagem)

        print(f'\nJARVIS: {resposta}\n')