# Questão 3
# Crie uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, desconsiderando espaços e pontuação).
def e_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

frase1 = "ana"
frase2 = "abba"
frase3 = "teste"

print(e_palindromo(frase1)) 
print(e_palindromo(frase2))
print(e_palindromo(frase3))
