# Questão 1
# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado "calcular_area" que retorna a área do círculo.
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2