# Questão 1
# Escreva um programa que recebe cinco notas de um aluno e calcula a média. 
# Em seguida, exiba se o aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")