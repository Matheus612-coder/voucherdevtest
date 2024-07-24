# Crie uma função que receba a altura e o raio de um cilindro circular e retorne o volume do 
# cilindro. O volume de um cilindro circular e calculado por meio da seguinte fórmula: 
# V = π ∗ raio2 ∗ altura, onde π = 3.141592.

def volume(altura,raio):
    volume= 3.141592 * raio**2 *altura
    print(f"{volume: .2f}")

altura = int(input("Digite a altura: "))
raio = int(input("Digite o raio: "))

volume(altura, raio)