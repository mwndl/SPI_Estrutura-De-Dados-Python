# Questão 4
# Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
def segundo_menor(vetor):
    vetor_unico = list(set(vetor))
    vetor_unico.sort()
    if len(vetor_unico) >= 2:
        return vetor_unico[1]
    else:
        return None
    
# Exemplo de uso:
vetor4 = [64, 25, 12, 22, 11, 25]
segundo_menor_numero = segundo_menor(vetor4)
print("Segundo menor número:", segundo_menor_numero)