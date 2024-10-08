# Crie uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus 
# Fahrenheit. A fórmula de conversão é: F = C ∗ (9.0/5.0) + 32.0, sendo F a temperatura em 
# Fahrenheit e C a temperatura em Celsius.

def conversao(celsius):
    convertido = celsius*(9/5)+32
    print(convertido, "graus farenheit")

celsius = int(input("Digite o valor em graus celsius: "))

conversao(celsius)






