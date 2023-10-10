# Questão 8
# Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do meio quando o vetor é ordenado.
# Certifique-se de que sua função funcione para vetores com um número ímpar de elementos.
def mediana(vetor):
    vetor.sort()
    meio = len(vetor) // 2
    if len(vetor) % 2 == 1:
        return vetor[meio]
    else:
        return (vetor[meio - 1] + vetor[meio]) / 2

# Exemplo de uso:
vetor8 = [7, 2, 5, 8, 3]
mediana_valor = mediana(vetor8)
print("Mediana:", mediana_valor)