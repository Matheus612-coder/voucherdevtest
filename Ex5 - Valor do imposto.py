def somaImposto(taxaImposto,custo):
     print(f"O produto antes do imposto custava {custo} reais e agora custa {(taxaImposto/100) * custo + custo} reais com {taxaImposto/100}% de imposto")

taxaImposto = float(input("Quanto é o imposto? "))
custo = float(input("Quanto custava o produto? "))


somaImposto(taxaImposto, custo)
