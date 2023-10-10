# Questão 10
# Escreva uma função que gera a sequência Fibonacci até um valor inserido pelo usuário.
def sequencia_fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

valor_limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))
fibonacci_resultado = sequencia_fibonacci(valor_limite)
print(f"Sequência de Fibonacci até {valor_limite}: {fibonacci_resultado}")