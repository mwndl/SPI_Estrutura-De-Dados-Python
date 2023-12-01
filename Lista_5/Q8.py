# Questão 8: "Desfazer" e "Refazer" em um Programa de Edição de Texto
class EditorDeTextoComHistorico:
    def __init__(self):
        self.historico_desfazer = []
        self.historico_refazer = []
        self.texto = ""

    def executar_comando(self, comando):
        self.historico_desfazer.append(self.texto)
        self.texto += comando
        self.historico_refazer = []  # Limpa o histórico de refazer

    def desfazer(self):
        if self.historico_desfazer:
            comando_desfeito = self.historico_desfazer.pop()
            self.historico_refazer.append(self.texto)
            self.texto = comando_desfeito
            print(f"Desfazendo: {comando_desfeito}")

    def refazer(self):
        if self.historico_refazer:
            comando_refeito = self.historico_refazer.pop()
            self.historico_desfazer.append(self.texto)
            self.texto = comando_refeito
            print(f"Refazendo: {comando_refeito}")

    def exibir_texto(self):
        print(f"Texto Atual: {self.texto}")

editor_com_historico = EditorDeTextoComHistorico()
editor_com_historico.executar_comando("Adicionar Texto1 ")
editor_com_historico.executar_comando("Adicionar Texto2 ")
editor_com_historico.exibir_texto()
editor_com_historico.desfazer()
editor_com_historico.exibir_texto()
editor_com_historico.refazer()
editor_com_historico.exibir_texto()
