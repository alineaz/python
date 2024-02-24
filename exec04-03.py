# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.

import os 

numeros = []
num = ""

while True:
    num = input("Digite um número para ser validado ou X para encerrar: ")
    if num == "x":
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls") 
            
        print("Encerrando lista...")
        print("Total de número pares: ",len(numeros))
        print("Lista de números pares: ",numeros)
        break

    else:
        num = int(num)
        if (num % 2) == 0:
            numeros.append(num)
            print("Número par identificado.")
        else:
            print("Número descartado.")

    