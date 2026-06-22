from datetime import datetime
import os


LOG_FILE = 'logs/tools.log'


def registrar_log(tool, entrada, saida):

    os.makedirs('logs', exist_ok=True)

    with open(LOG_FILE, 'a', encoding='utf-8') as file:

        file.write(

            f'[{datetime.now()}] '

            f'TOOL={tool} | '

            f'INPUT={entrada} | '

            f'OUTPUT={saida}\n'

        )