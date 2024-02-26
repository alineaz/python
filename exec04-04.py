# Reescreva o exercício da quitanda do capítulo 2 separando as operações
# em funções, e adiconando um preço para cada fruta, de modo que quando a pessoa
# fizer o checkout ela consiga ver o preço total a pagar.
import os 

def limpa_tela():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def adiciona_fruta(fruta):
    global checkout
    if fruta == "1":
        limpa_tela()
        print("Adicionando uma banana à cesta")
        cesta.append("Banana")
        checkout += 2.50

    elif fruta == "2":
        limpa_tela()
        print("Adicionando uma melancia à cesta")
        cesta.append("Melancia")
        checkout += 6.00

    elif fruta == "3":
        limpa_tela()
        print("Adicionando um morango à cesta")
        cesta.append("Morango")
        checkout += 1.50
    else:
        limpa_tela()
        print("Voce digitou um valor invalido")

cesta = []
checkout = 0.0

while True:
    resposta = input("""
Quitanda:
1: Ver cesta
2: Adicionar frutas
3: Sair
""")

    if resposta == "1":
        limpa_tela()
        if len(cesta) == 0:
            print("Sua cesta ainda está vazia")
        else:
            print(f"A sua cesta atualmente possui: {cesta}")

    elif resposta == "2":
        limpa_tela()
        fruta = input("""
Escolha uma fruta:
1 - Banana
2 - Melancia
3 - Morango
""")
        adiciona_fruta(fruta)
    
    elif resposta == "3":
        limpa_tela()
        print("Parando o programa...")
        print(f"O total a pagar é de R${checkout:.2f}")
        break

    else:
        limpa_tela()
        print("Voce digitou um valor invalido")
