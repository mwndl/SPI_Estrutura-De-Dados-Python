# Questão 3
# Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.
def encontrar_maximo_minimo(vetor):
    maximo = vetor[0]
    minimo = vetor[0]
    for num in vetor:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num
    return maximo, minimo

# Exemplo de uso:
vetor3 = [64, 25, 12, 22, 11]
maximo, minimo = encontrar_maximo_minimo(vetor3)
print("Máximo:", maximo)
print("Mínimo:", minimo)