# Questão 4: Lista de Tarefas Pendentes
class ListaDeTarefas:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, tarefa):
        self.fila.append(tarefa)

    def concluir_tarefas(self):
        while self.fila:
            tarefa = self.fila.pop(0)
            print(f"Concluindo tarefa: {tarefa}")


lista_tarefas = ListaDeTarefas()
lista_tarefas.adicionar_tarefa("Estudar Python")
lista_tarefas.adicionar_tarefa("Fazer exercícios")
lista_tarefas.concluir_tarefas()
