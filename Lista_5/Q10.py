# Questão 10: Verificar se uma Palavra ou Frase é um Palíndromo
class VerificadorPalindromo:
    def __init__(self):
        self.pilha = []

    def eh_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        for caractere in texto:
            self.pilha.append(caractere)

        inverso = ""
        while self.pilha:
            inverso += self.pilha.pop()

        return texto == inverso

verificador_palindromo = VerificadorPalindromo()
resultado = verificador_palindromo.eh_palindromo("Anilina")
print(f"É um palíndromo: {resultado}")
