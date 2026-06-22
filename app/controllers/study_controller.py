from app.tools.agenda_tools import consultar_agenda
from app.tools.task_tools import tool_listar_tarefas
from app.tools.rag_tools import buscar_material_rag


class StudyController:

    def obter_contexto_estudos(self, tema=None):

        agenda = consultar_agenda()

        tarefas = tool_listar_tarefas()

        materiais = ""

        if tema:
            materiais = buscar_material_rag(tema)

        return {
            "agenda": agenda,
            "tarefas": tarefas,
            "materiais": materiais
        }

    def gerar_plano_estudos(self, tema=None):

        contexto = self.obter_contexto_estudos(tema)

        plano_estudos = f"""
PLANO DE ESTUDOS: {tema}

========================
AGENDA ACADÊMICA
========================

{contexto['agenda']}

========================
TAREFAS PENDENTES
========================

{contexto['tarefas']}
"""

        if contexto["materiais"]:

            plano_estudos += f"""

========================
MATERIAIS RELEVANTES
========================

{contexto['materiais']}
"""

        plano_estudos += f"""

========================
PLANO RECOMENDADO
========================

Hoje:
- Revisar os conceitos principais sobre {tema}
- Resolver exercícios básicos
- Fazer anotações importantes

Amanhã:
- Revisar tópicos mais difíceis
- Resolver exercícios intermediários
- Criar resumo do conteúdo

Próximos dias:
- Fazer simulado
- Revisão geral
- Revisão final antes da prova
"""

        return plano_estudos
