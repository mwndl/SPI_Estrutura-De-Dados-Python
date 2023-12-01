# Questão 7: Calculadora RPN (Notação Polonesa Reversa)
class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar_expressao_rpn(self, expressao):
        tokens = expressao.split()
        for token in tokens:
            if token.isdigit():
                self.pilha.append(int(token))
            else:
                operando2 = self.pilha.pop()
                operando1 = self.pilha.pop()
                if token == '+':
                    self.pilha.append(operando1 + operando2)
                elif token == '-':
                    self.pilha.append(operando1 - operando2)
                elif token == '*':
                    self.pilha.append(operando1 * operando2)
                elif token == '/':
                    self.pilha.append(operando1 / operando2)
        return self.pilha.pop()


calculadora_rpn = CalculadoraRPN()
resultado = calculadora_rpn.avaliar_expressao_rpn("3 4 + 2 *")
print(f"Resultado: {resultado}")
