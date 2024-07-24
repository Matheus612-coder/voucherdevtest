# Crie uma função de um programa de teste para o cálculo do volume de uma esfera. Sendo que o 
# raio é passado por parâmetro?
# V = 4/3 ∗ π ∗ R3

def area(raio):
    volume = 4/3 *3.14 * raio**3
    print(f"VOLUME: {volume:.2f}")

area(int(input("Qual o raio da esfera? ")))




