# Questão 8
# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)