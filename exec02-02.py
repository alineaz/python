# 2) Escreva um script em Python que receba dois números e que seja realizado as seguintes operações:
# soma dos dois numeros 
# diferença dos dois numeros 
# o resultado deverá ser apresentado conforme a seguir: 

# -----------------------------------------
# Soma: 4 + 2 = 6
# Diferença: 4 -2 = 2 

num1 = input("Digite primeiro número: ")
num2 = input("Digite o segundo número: ")
num1 = float(num1)
num2 = float(num2)
soma = num1 + num2 
menos = num1 - num2 

print(40*"-")
print("Soma: ",num1," + ",num2," = ",soma)
print("Diferença: ",num1," - ",num2," = ",menos)
print(40*"-")