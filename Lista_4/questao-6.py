# Questão 6
# Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte quantos números pares e quantos números ímpares existem no vetor ordenado.
def contar_pares_impares(vetor):
    vetor.sort(reverse=True)
    pares = 0
    impares = 0
    for num in vetor:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

# Exemplo de uso:
vetor6 = [7, 2, 5, 8, 3, 9, 6]
pares, impares = contar_pares_impares(vetor6)
print("Pares:", pares)
print("Ímpares:", impares)