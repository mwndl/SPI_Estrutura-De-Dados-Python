# Questão 1: Fila de Impressão
class FilaDeImpressao:
    def __init__(self):
        self.fila = []

    def adicionar_documento(self, documento):
        self.fila.append(documento)

    def imprimir_documentos(self):
        while self.fila:
            documento = self.fila.pop(0)
            print(f"Imprimindo documento: {documento}")


fila_impressao = FilaDeImpressao()
fila_impressao.adicionar_documento("Documento1")
fila_impressao.adicionar_documento("Documento2")
fila_impressao.imprimir_documentos()
