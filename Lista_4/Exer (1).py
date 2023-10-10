# Questão 5
# Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos duplicados, retornando o vetor resultante sem duplicatas.
def remover_duplicatas(vetor):
    return list(set(vetor))

# Exemplo de uso:
vetor5 = [1, 2, 2, 3, 4, 4, 5]
vetor_sem_duplicatas = remover_duplicatas(vetor5)
print("Vetor sem duplicatas:", vetor_sem_duplicatas)