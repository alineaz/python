# ===========================================================================================
# 2) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

# São 2587 ao todo.

# Tupla      = ()
# Lista      = []
# Dicionario = {chave:valor}
# Set        = {chave}

def checaVogal(letra): 
    if letra.lower() in "aeiouáéíóúãẽĩõũâêîôûàèìòùäëïöü":
        return True 
    else: 
        return False 
    
vogais = 0
consoantes = set() 

with open("faroeste.txt","r",encoding="UTF-8") as arquivo:
    conteudo = arquivo.read() 

    for letra in conteudo:
        if checaVogal(letra) == True:
            vogais += 1
        else:
            consoantes.add(letra)

print(f"Vogais: {vogais}")
print(f"Não vogais: \n{consoantes}")

