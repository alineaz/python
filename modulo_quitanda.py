import os 

def limpa_tela():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def adiciona_fruta(fruta, cesta, checkout):
    #global checkout
    if fruta == "1":
        limpa_tela()
        print("Adicionando uma banana à cesta")
        cesta.append("Banana")
        checkout += 2.50
        return checkout

    elif fruta == "2":
        limpa_tela()
        print("Adicionando uma melancia à cesta")
        cesta.append("Melancia")
        checkout += 6.00
        return checkout

    elif fruta == "3":
        limpa_tela()
        print("Adicionando um morango à cesta")
        cesta.append("Morango")
        checkout += 1.50
        return checkout
    else:
        limpa_tela()
        print("Voce digitou um valor invalido")