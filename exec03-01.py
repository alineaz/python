# Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# Menu principal:

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair

# Menu de frutas:
# Digite a opção desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem:
# Digitado uma opção inválida

# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.
import os 

cesta = []

while True:
    resposta = input("""
Menu da quitandinha:
1: Ver cesta
2: Adicionar frutas
3: Sair
""")

    if resposta == "1":

        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    
        if len(cesta) == 0:
            print("Cesta vazia.")

        else:
            print(f"A sua cesta possui atualmente: {cesta}")
    
    elif resposta =="2":

        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        
        fruta = input("""
                      Escolha uma fruta:
                      1 - Banana
                      2 - Melancia
                      3 - Morango
                      """)
        if fruta == "1":
            cesta.append("Banana")
            print("Banana adicionada com sucesso!")
        elif fruta == "2":
            cesta.append("Melancia")
            print("Melancia adicionada com sucesso!")
        elif fruta == "3":
            cesta.append("Morango")
            print("Morango adicionado com sucesso!")
        else:
            print("Opção inválida")


    elif resposta == "3":

        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls") 

        print("Parando o programa.")
        break

    else:
        print("Você digitou um valor inválido.")