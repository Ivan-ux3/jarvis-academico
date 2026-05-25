from app.models.db import get_connection


def adicionar_tarefa(descricao):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO tarefas (descricao) VALUES (?)',
        (descricao,)
    )

    conn.commit()
    conn.close()


def listar_tarefas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tarefas')

    tarefas = cursor.fetchall()

    conn.close()

    return tarefas


def concluir_tarefa(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE tarefas SET status = ? WHERE id = ?',
        ('concluida', task_id)
    )

    conn.commit()
    conn.close()