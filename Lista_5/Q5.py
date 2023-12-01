# Questão 5: Fila de Pedidos Online em Comércio Eletrônico
class FilaDePedidosOnline:
    def __init__(self):
        self.fila = []

    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)

    def processar_pedidos_online(self):
        while self.fila:
            pedido = self.fila.pop(0)
            print(f"Processando pedido online: {pedido}")


fila_pedidos_online = FilaDePedidosOnline()
fila_pedidos_online.adicionar_pedido("Pedido1")
fila_pedidos_online.adicionar_pedido("Pedido2")
fila_pedidos_online.processar_pedidos_online()
