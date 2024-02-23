# Anotações da aula 03

# Coleções: 
# Tuplas, Listas, Dicionarios, Sets 

# Tuplas: 
# parentesis
# coleção de vários itens individuais
# tipos podem ser variados (string, inteiros, ate mesmo outra tupla)
# tuplas sao imutaveis
# tem index (0, 1, 2, 3)

variavel1 = ("Arroz","Queijo","Leite","Beterraba")
print(variavel1)

for item in variavel1:
    print(item)

print(variavel1[2])

# Listas 
# Listas são mutáveis, diferentes da tupla 

variavel2 = ["Banana","Maça","Limão","Laranja"]

print(variavel2[3])

variavel2.append("Melancia") # adiciona item no final
variavel2.insert(0,"Abacate") # adiciona item no index escolhido

print(variavel2)

for item in enumerate(variavel2):
    print(item)

#Dicionarios: # Hash tables


#             CHAVE:VALOR   CHAVE:VALOR        CHAVE:VALOR  
variavel3 = {"idade": 35, "cor": "preto", "animal": "gato"}
#            |----------| |----------------| |--------------|
#                ITEM              ITEM             ITEM

for x in variavel3["idade"]:
    if x >= 18:
        print(x)

variavel3["nome"] = "Tiago" #Adicionando um item no dicionario, com a chave "nome" e valor "Tiago"

variavel3.pop("idade")      #Removendo um valor do dicionario com o metodo .pop
del(variavel3["cor"])       #Removendo um valor do dicionario com a função del

print(variavel3)

for objeto in variavel3.values():
    print(objeto)

# Não podem haver chaves repetidas em um dicionario

# =========
#Sets:

variavel4 = ["idade", "cachorro", 12, False, 500, "idade", 12] #LISTA
variavel4 = set(variavel4)                                     # Convertendo em SET
variavel4 = list(variavel4)                                    # Convertendo em LISTA

print(variavel4)
