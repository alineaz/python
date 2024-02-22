# ====================================================
# Escreva uma calculadora utilizando funções
# Ela pergunta dois numeros, e da as opções de calculo.
# (soma, diferença, multiplicação, divisão)

def soma(num1, num2):
    soma = num1 + num2
    return soma 

def difer(num1, num2):
    difer = num1 - num2 
    return difer 

def multi(num1, num2):
    multi = num1 * num2
    return multi 

def divisao(num1, num2):
    divisao = num1 / num2 
    return divisao

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num1 = float(num1) 
num2 = float(num2)

print(40*"-")
print("1 - Soma")
print("2 - Diferença")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = input("Escolha qual função deseja utilizar: ")
print(40*"-")
 

if escolha == "1":
    resultado = soma(num1,num2) 
    print("O resultado da soma é",resultado)

if escolha == "2":
    resultado = difer(num1,num2) 
    print("O resultado da diferença é",resultado)

if escolha == "3":
    resultado = multi(num1,num2) 
    print("O resultado da multiplicação é",resultado)

if escolha == "4":
    resultado = divisao(num1,num2) 
    print("O resultado da divisão é",resultado)

