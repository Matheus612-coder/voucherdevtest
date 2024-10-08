# Elabore uma função que receba dois valores numéricos e um símbolo. Este símbolo representara 
# a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma 
# adição, se for − uma subtração, se for / uma divisão e se for ∗ será efetuada uma multiplicação.

def calculadora(num,num2,simbolo):
    
    if simbolo == "+":
        print(num+num2)

    elif simbolo == "-":
        print(num-num2)

    elif simbolo == "*":
        print(num*num2)

    else:
        print(num/num2)

num = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
simbolo = input("Digite um dos símbolos: + , -, *, / : ")

calculadora(num, num2, simbolo)



