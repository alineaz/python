# Aula 02
# Tipos primitivos - tipos de dados básicos do python

# String: -> str -> frases ou conjunto de caracteres, sempre entre aspas.
# Integer -> int -> numeros inteiros, sem aspas.
# Float -> float -> numeros decimais (numeros com virgula)
# Boolean -> bool -> true ou false  

# Operadores aritmeticos:
# + - * / 

# Operadores de comparação:
# igualdade -> == 
# desigualdade -> !=
# maior que -> 
# menor que <-

# Exemplos 

nome = "Aline A. Rocha" #string 
idade = 33 #int 
altura = 1.57 #float
acordado = True #bool

frase = "Uma gota d'agua" # aspas dentro da frase, usar dupla por fora

#convert to string
idade = str(idade)

# Metodos de strings 
nome2 = "Aline Azevedo Rocha"
#print(nome2.replace("A","M"))
#print(nome2.upper())

# Estruturas de repetição

#idade = int(input("Digite sua idade: "))

#if idade >= 18:
#    print("Você pode entrar!")
#else:
#    print("Ainda menor de idade.")

idade = 18
while idade <= 17:
    print("Você é muito novo pra entrar.")
    idade = int(input("Qual a sua idade? "))

contador = 18
while contador < 11:
    print("Contando ",contador," vezes." )
    contador = contador+1

while True:
    resposta = input("Parar programa? S/N ")
    if resposta == "S":
        break

for numero in range(0, 10):
    print(numero)

for letra in "Aline Rocha":
    print(letra)