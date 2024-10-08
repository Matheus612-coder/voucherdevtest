# Elabore uma função que receba a distância em Km e a quantidade de litros de gasolina 
# consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma 
# mensagem de acordo com a tabela abaixo:
# Consumo Km/l Mensagem
# menor que 8 Gasta muito!
# entre 8 e 15 Econômico!
# maior que 15 Super econômico!


def consumo():
        
        try:
            litro= float(input("Digite a quantidade de gasolina consumida: "))
            quilometro= float(input("Digite quantos quilômetros o carro andou antes de perder um nível: "))
            consumo = quilometro/litro
            
            if consumo < 8:
                print("Gasta muito.")
        

            elif consumo ==8 or consumo <=15:
                print("Econômico.")

            else:
                print("Super econômico.")
        
        except:
            print("Digite apenas números!")

consumo()









