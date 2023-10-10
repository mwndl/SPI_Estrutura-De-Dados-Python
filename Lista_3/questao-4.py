# Questão 4
# Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.
numero = int(input("Digite um número inteiro positivo: "))
soma = sum(map(int, str(numero)))
print(f"A soma dos dígitos de {numero} é: {soma}")