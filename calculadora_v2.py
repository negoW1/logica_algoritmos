saida = ""
def adicao(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b ==0:
        print("Não foi possível realizar a divisão por 0")
    else:
        return a/b
    
def calculadora(a,b,operacao):
    if operacao.lower() == "adição" or operacao == "+":
        resultado = adicao(a,b)
    elif operacao.lower() == "subtração" or operacao == "-":
        resultado = subtracao(a,b)
    elif operacao.lower() == "multiplicação" or operacao == "*":
        resultado = multiplicacao(a,b)
    elif operacao.lower() == "divisão" or operacao == "/":
        resultado=divisao(a,b)
    
    return resultado

while saida.lower() != "n":
    a=int(input("digite o primeiro numero: "))
    b=int(input("digite o segundo numero: "))
    operacao=input("digite a operacao matematica: ")
    resultado = calculadora(a,b,operacao)
    print(f"Resultado da operação: {resultado}")
    saida=input("deseja  continuar executando o programa ? [s/n]")



    

    
    

           
    
