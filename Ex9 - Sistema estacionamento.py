def calcularTempo(tempo):

    if tempo <15:
        print ("Valor não cobrado.")
    
    else: 
        if tempo % 60 ==0:
            valor = (tempo/60) * 9
            print(valor, "reais")
           
            tempo_extra = input("Precisa de tempo adicional? ")

            if tempo_extra == "s".lower() or tempo_extra == "sim".lower():
                
                novotempo =int(input("Digite o tempo adicional em minutos: "))

                if novotempo <15:
                    print("Valor não cobrado.")

                else:
                    if novotempo %60 == 0:

                        tempodividido = novotempo/60


                        novovalor = valor + 1.5*tempodividido
                        print(novovalor, "reais")

            else:
                print(valor, "reais")  

         
calcularTempo(int(input("Digite o tempo em minutos: ")))        