# Questão 6: Navegador Web Simplificado com Pilha para Histórico
class NavegadorWebSimplificado:
    def __init__(self):
        self.historico = []
        self.indice_atual = -1

    def visitar_pagina(self, pagina):
        self.historico = self.historico[:self.indice_atual + 1]
        self.historico.append(pagina)
        self.indice_atual += 1

    def voltar_pagina(self):
        if self.indice_atual > 0:
            self.indice_atual -= 1
            print(f"Voltando para a página: {self.historico[self.indice_atual]}")

    def avancar_pagina(self):
        if self.indice_atual < len(self.historico) - 1:
            self.indice_atual += 1
            print(f"Avançando para a página: {self.historico[self.indice_atual]}")


navegador_simplificado = NavegadorWebSimplificado()
navegador_simplificado.visitar_pagina("www.google.com")
navegador_simplificado.visitar_pagina("www.wikipedia.org")
navegador_simplificado.voltar_pagina()
navegador_simplificado.avancar_pagina()
