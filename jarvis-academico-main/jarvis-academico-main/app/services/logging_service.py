from datetime import datetime

LOG_FILE = 'logs/tools.log'


def registrar_log(tool, entrada, saida):
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(
            f'[{datetime.now()}] TOOL={tool} | INPUT={entrada} | OUTPUT={saida}\n'
        )