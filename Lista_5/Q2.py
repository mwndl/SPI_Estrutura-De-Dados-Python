# Questão 2: Fila de Atendimento Bancário
class FilaDeAtendimento:
    def __init__(self):
        self.fila = []

    def entrar_na_fila(self, cliente):
        self.fila.append(cliente)

    def atender_clientes(self):
        while self.fila:
            cliente = self.fila.pop(0)
            print(f"Atendendo cliente: {cliente}")


fila_atendimento = FilaDeAtendimento()
fila_atendimento.entrar_na_fila("Cliente1")
fila_atendimento.entrar_na_fila("Cliente2")
fila_atendimento.atender_clientes()
