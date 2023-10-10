# Questão 7
# Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
def terceiro_maior(vetor):
    vetor_unico = list(set(vetor))
    if len(vetor_unico) >= 3:
        vetor_unico.sort()
        return vetor_unico[-3]
    else:
        return None

# Exemplo de uso:
vetor7 = [64, 25, 12, 22, 11, 25, 64]
terceiro_maior_numero = terceiro_maior(vetor7)
print("Terceiro maior número:", terceiro_maior_numero)