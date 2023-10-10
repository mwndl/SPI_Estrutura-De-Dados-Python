# Questão 1
# Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o algoritmo de seleção.
def ordenar_selecao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

# Exemplo de uso:
vetor1 = [64, 25, 12, 22, 11]
ordenar_selecao(vetor1)
print("Vetor ordenado pelo algoritmo de seleção:", vetor1)