# 1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como nome, CPF, idade e unidade federativa.
# Escreva um script em python que solicite as informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# --------------------------------------------
# Confirmação de cadastro:
# Nome: Guido Van Rossum 
# CPF: 999.888.777/66
# Idade: 65 
# --------------------------------------------

print("Olá, seja bem vindo ao cadastro de novos usuários!")
print("Prencha os dados conforme solicitado. ")
nome = input("Digite o nome completo: ")
cpf = input("Digite o seu CPF: ")
idade = input("Digite sua idade: ")
print(60*'-')
print("Confirmação de cadastro: ")
print("Nome: ",nome)
print("CPF: ",cpf)
print("Idade: ",idade)
print(60*'-')