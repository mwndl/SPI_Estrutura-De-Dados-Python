# Questão 2
# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que serve como chave para realizar a ordenação crescente ou decrescente.
def ordenar_vetor(vetor, chave):
    vetor.sort(reverse=(chave == 'decrescente'))

# Exemplo de uso:
vetor2 = [64, 25, 12, 22, 11]
ordenar_vetor(vetor2, 'crescente')
print("Vetor ordenado em ordem crescente:", vetor2)