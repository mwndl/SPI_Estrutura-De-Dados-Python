# Questão 8
# Escreva um programa que converte uma temperatura em Celsius para Fahrenheit ou vice-versa, dependendo da escolha do usuário.
opcao = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").upper()
temperatura = float(input("Digite a temperatura: "))

if opcao == 'C':
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura}°C é igual a {fahrenheit}°F")
elif opcao == 'F':
    celsius = (temperatura - 32) * 5/9
    print(f"{temperatura}°F é igual a {celsius}°C")