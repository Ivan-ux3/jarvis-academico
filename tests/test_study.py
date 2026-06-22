from unittest.mock import patch

from app.controllers.study_controller import StudyController
from app.tools.study_tools import (
    consultar_contexto_estudos,
    planejar_estudos
)

controller = StudyController()


# =========================
# TESTE DO CONTROLLER
# =========================

@patch(
    "app.controllers.study_controller.buscar_material_rag"
)
@patch(
    "app.controllers.study_controller.tool_listar_tarefas"
)
@patch(
    "app.controllers.study_controller.consultar_agenda"
)
def test_obter_contexto_estudos(
    mock_agenda,
    mock_tarefas,
    mock_rag
):

    mock_agenda.return_value = (
        "1 - Prova de IA | 2026-06-25 | prova"
    )

    mock_tarefas.return_value = (
        "1 - Estudar AVL (pendente)"
    )

    mock_rag.return_value = (
        "Árvores AVL são árvores balanceadas."
    )

    resultado = controller.obter_contexto_estudos(
        "Árvores AVL"
    )

    assert resultado is not None

    assert isinstance(resultado, dict)

    assert "agenda" in resultado

    assert "tarefas" in resultado

    assert "materiais" in resultado


@patch(
    "app.controllers.study_controller.buscar_material_rag"
)
@patch(
    "app.controllers.study_controller.tool_listar_tarefas"
)
@patch(
    "app.controllers.study_controller.consultar_agenda"
)
def test_gerar_plano_estudos(
    mock_agenda,
    mock_tarefas,
    mock_rag
):

    mock_agenda.return_value = (
        "1 - Prova de IA | 2026-06-25 | prova"
    )

    mock_tarefas.return_value = (
        "1 - Estudar AVL (pendente)"
    )

    mock_rag.return_value = (
        "Conteúdo mockado de AVL."
    )

    resultado = controller.gerar_plano_estudos(
        "Árvores AVL"
    )

    assert resultado is not None

    assert isinstance(resultado, str)

    assert "PLANO DE ESTUDOS" in resultado

    assert "Hoje:" in resultado

    assert "Amanhã:" in resultado


# =========================
# TESTE DAS TOOLS
# =========================

@patch(
    "app.tools.study_tools.registrar_log"
)
@patch(
    "app.controllers.study_controller.buscar_material_rag"
)
@patch(
    "app.controllers.study_controller.tool_listar_tarefas"
)
@patch(
    "app.controllers.study_controller.consultar_agenda"
)
def test_consultar_contexto_estudos(
    mock_agenda,
    mock_tarefas,
    mock_rag,
    mock_log
):

    mock_agenda.return_value = (
        "1 - Prova de IA | 2026-06-25 | prova"
    )

    mock_tarefas.return_value = (
        "1 - Estudar AVL (pendente)"
    )

    mock_rag.return_value = (
        "Material AVL mockado."
    )

    resultado = consultar_contexto_estudos(
        "Árvores AVL"
    )

    assert resultado is not None

    assert isinstance(resultado, dict)

    assert "agenda" in resultado

    assert "tarefas" in resultado

    assert "materiais" in resultado


@patch(
    "app.tools.study_tools.registrar_log"
)
@patch(
    "app.controllers.study_controller.buscar_material_rag"
)
@patch(
    "app.controllers.study_controller.tool_listar_tarefas"
)
@patch(
    "app.controllers.study_controller.consultar_agenda"
)
def test_planejar_estudos(
    mock_agenda,
    mock_tarefas,
    mock_rag,
    mock_log
):

    mock_agenda.return_value = (
        "1 - Prova de IA | 2026-06-25 | prova"
    )

    mock_tarefas.return_value = (
        "1 - Estudar AVL (pendente)"
    )

    mock_rag.return_value = (
        "Material AVL mockado."
    )

    resultado = planejar_estudos(
        "Árvores AVL"
    )

    assert resultado is not None

    assert isinstance(resultado, str)

    assert "PLANO DE ESTUDOS" in resultado

    assert "Hoje:" in resultado

    assert "Amanhã:" in resultado
