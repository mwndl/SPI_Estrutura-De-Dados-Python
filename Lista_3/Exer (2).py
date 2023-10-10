# Questão 9
# Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base na escolha do usuário.
def calcular(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Divisão por zero não é permitida."

operacao = input("Digite a operação (+, -, *, /): ")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = calcular(operacao, numero1, numero2)
print(f"Resultado: {resultado}")