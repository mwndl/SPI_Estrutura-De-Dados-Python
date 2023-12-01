# Questão 3: Gerenciamento de Pedidos em um Restaurante
class FilaDePedidos:
    def __init__(self):
        self.fila = []

    def fazer_pedido(self, pedido):
        self.fila.append(pedido)

    def processar_pedidos(self):
        while self.fila:
            pedido = self.fila.pop(0)
            print(f"Processando pedido: {pedido}")


fila_pedidos = FilaDePedidos()
fila_pedidos.fazer_pedido("Pizza")
fila_pedidos.fazer_pedido("Bebida")
fila_pedidos.processar_pedidos()
