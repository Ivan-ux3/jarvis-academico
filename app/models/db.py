import sqlite3


DATABASE_NAME = 'jarvis.db'


def get_connection():

    conn = sqlite3.connect(
        DATABASE_NAME,
        timeout=30
    )

    conn.row_factory = sqlite3.Row

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tarefas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            descricao TEXT NOT NULL,

            status TEXT NOT NULL

        )
        '''
    )


    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS agenda (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT NOT NULL,

            data TEXT NOT NULL,

            tipo TEXT NOT NULL

        )
        '''
    )


    conn.commit()

    conn.close()


# Garante que as tabelas existam
create_tables()