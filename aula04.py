import os 
import flask # utilizado para criar APIs
import modulo_baixado #importa todos os modulos
from modulo_baixado import imprime_mensagem # apenas 1 modulo, imprime mensagem

# Aula de funções: trechos de codigos que podem ser reutilizados ao longo do programa. 
# Exemplo: limpa tela

def limpa_tela():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

print("""Teste
      Teste
      Teste""")

limpa_tela() 

def boas_vindas():
    nome = input("Qual é o seu nome? ")
    print(f"Seja muito bem vindo {nome}!")

boas_vindas()

# Criando um UNICO parametro capaz de armazenar um numero indefinido de valores:
def mult(*x, y):
    for valor in x:
        print(f"{valor} x {y} = {valor * y}")

mult(10, 32, 2, 10, 12, y=5)

# ===============================================
# Criando um numero indefinido de parametros:
def diff(a, **chaves):
    for valor in chaves.values():
        print(f"{a} - {valor} = {a - valor}")

diff(a=75, b=20, c=45, d=120)
diff(a=10, b=20, c=45)
diff(a=10, b=20, c=45, d=120, e=500, f=450)


# funções Lambda/Anonimas

def soma1(x,y):
    return(x + y)

soma2 = lambda x,y: x + y #a função está dentro da variavel soma2

print(soma1(10,15))
print(soma2(10,15))


# Modulos em Python 
# Trecho de codigos, como funções
# 3 maneiras de  acesso a novos módulos no Python
# existem nativos e carregados (print, input, etc)
# existem nativos e não carregados (os, math, random)
# existem nao-nativos que precisam ser baixados pelo gerenciador pip (flask, pymongo) (pip install flask)
# download da comunidade (githubs, etc)

modulo_baixado.imprime_mensagem()