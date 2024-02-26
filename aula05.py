import csv 

# Trabalhando com arquivos 
# w - write, faz overwrite em cima do arquivo
# r - read
# a - append, adicionar conteudo sem sobescrever

arquivo = open("teste.txt","a")  # abrir arquivo ou criação se não existir
conteudo = "Primeira linha do meu arquivo.\n" # adicionando conteudo na variavel
arquivo.write(conteudo) # gravando conteudo no arquivo
arquivo.close() # fechando arquivo 

arquivo = open("teste.txt","r")
conteudo = arquivo.read() 
#print(conteudo)
arquivo.close()

with open("teste.txt","a") as arquivo:
    conteudo = "\n Linha adicionada com WITH \n" # adicionando conteudo na variavel
    arquivo.write(conteudo) # gravando conteudo no arquivo
#print("Finalizado")

# ===========================
# CSV

with open("arquivo.csv","r") as planilha:
    conteudo = csv.reader(planilha,delimiter=";")
    #generator 
    #print(next(conteudo))
    for linha in conteudo:
        print(linha)

# ===========================