
# Questão 6
# Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes nela.
texto = input("Digite uma string: ").lower()
vogais = "aeiou"
contagem = sum(texto.count(vogal) for vogal in vogais)
print(f"A quantidade de vogais na string é: {contagem}")