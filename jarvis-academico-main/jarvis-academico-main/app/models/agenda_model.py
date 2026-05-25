from app.models.db import get_connection


def adicionar_evento(titulo, data, tipo):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO agenda (titulo, data, tipo)
        VALUES (?, ?, ?)
        ''',
        (titulo, data, tipo)
    )

    conn.commit()

    conn.close()


def listar_eventos():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM agenda')

    eventos = cursor.fetchall()

    conn.close()

    return eventos