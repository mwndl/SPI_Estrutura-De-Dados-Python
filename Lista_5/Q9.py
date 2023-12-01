# Questão 9: Identificar Operadores em Expressão Matemática
class IdentificadorOperadores:
    def __init__(self):
        self.pilha = []

    def identificar_operadores(self, expressao):
        for caractere in expressao:
            if caractere in "+-*/^":
                self.pilha.append(caractere)

        return self.pilha

identificador = IdentificadorOperadores()
operadores = identificador.identificar_operadores("(2+3)*(8-9)/(7^3)")
print(f"Operadores encontrados: {operadores}")
