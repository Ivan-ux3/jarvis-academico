import unittest
from unittest.mock import patch

from app.tools.study_tools import gerar_plano_estudos


class TestStudyTools(unittest.TestCase):


    @patch('app.tools.study_tools.consultar_agenda')
    @patch('app.tools.study_tools.tool_listar_tarefas')
    @patch('app.tools.study_tools.buscar_documentos')
    def test_agenda_vazia(
            self,
            mock_documentos,
            mock_tarefas,
            mock_agenda
    ):

        mock_agenda.return_value = 'Nenhum evento encontrado.'
        mock_tarefas.return_value = '1 - Estudar TCP (pendente)'
        mock_documentos.return_value = ['Material TCP']

        resultado = gerar_plano_estudos()

        self.assertIn(
            'Nenhuma prova agendada',
            resultado
        )


    @patch('app.tools.study_tools.consultar_agenda')
    @patch('app.tools.study_tools.tool_listar_tarefas')
    @patch('app.tools.study_tools.buscar_documentos')
    def test_sem_tarefas_pendentes(
            self,
            mock_documentos,
            mock_tarefas,
            mock_agenda
    ):

        mock_agenda.return_value = (
            '1 - Prova Redes | 2026-06-30 | prova'
        )

        mock_tarefas.return_value = (
            'Nenhuma tarefa encontrada.'
        )

        mock_documentos.return_value = [
            'Material TCP'
        ]


        resultado = gerar_plano_estudos()


        self.assertIn(
            'Nenhuma tarefa pendente',
            resultado
        )


    @patch('app.tools.study_tools.consultar_agenda')
    @patch('app.tools.study_tools.tool_listar_tarefas')
    @patch('app.tools.study_tools.buscar_documentos')
    def test_prova_proxima(
            self,
            mock_documentos,
            mock_tarefas,
            mock_agenda
    ):

        mock_agenda.return_value = (
            '1 - Prova Redes | amanhã | prova'
        )

        mock_tarefas.return_value = (
            '1 - Estudar TCP (pendente)'
        )

        mock_documentos.return_value = [
            'Material TCP'
        ]


        resultado = gerar_plano_estudos()


        self.assertIsNotNone(resultado)


    @patch('app.tools.study_tools.consultar_agenda')
    @patch('app.tools.study_tools.tool_listar_tarefas')
    @patch('app.tools.study_tools.buscar_documentos')
    def test_multiplas_tarefas(
            self,
            mock_documentos,
            mock_tarefas,
            mock_agenda
    ):

        mock_agenda.return_value = (
            '1 - Prova Redes'
        )

        mock_tarefas.return_value = '''

1 - Estudar TCP
2 - Revisar UDP
3 - Fazer exercícios

'''

        mock_documentos.return_value = [
            'Material TCP'
        ]


        resultado = gerar_plano_estudos()


        self.assertIn(
            'Priorize tarefas pendentes',
            resultado
        )


    @patch('app.tools.study_tools.buscar_documentos')
    def test_falha_recuperacao_materiais(
            self,
            mock_documentos
    ):

        mock_documentos.side_effect = Exception(
            'Falha'
        )


        resultado = gerar_plano_estudos()


        self.assertIn(
            'Erro',
            resultado
        )



if __name__ == '__main__':
    unittest.main()