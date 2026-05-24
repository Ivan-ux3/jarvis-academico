from app.models.db import create_tables

from app.views.cli_view import iniciar_chat


def main():

    create_tables()

    iniciar_chat()


if __name__ == '__main__':
    main()