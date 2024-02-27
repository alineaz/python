# Aula 06 - Programação Orientada a Objetos

# Classes (tipos de objetos)

# Criação de uma classe(tipo de objeto) para simular uma pilha. 

class Pilha: # classes começam com letra maiuscula 

    def __init__(self): # função que inicializa uma classe e adiciona caracteristicas a esse objeto Pilha 
        self.pilha = list()
        self.limite = 5
        self.quantidade = 0 
    
    def empilhar(self, item):
        if self.quantidade < 5:
            self.pilha.append(item)
            self.quantidade += 1 
            return(f"{item} adicionado à pilha.")
        else:
            return(f"Essa pilha já tem {self.quantidade} items.")

    def desempilhar(self): 
        if self.quantidade > 0: 
           del self.pilha[-1]
           self.quantidade -= 1
           return(f"Item removido.")
        else:
           return(f"A pilha ja está vazia!")


variavel1 = Pilha() # variavel tipo Pilha, criada acima 
variavel2 = Pilha() 
variavel3 = Pilha()

#print(variavel1.limite)
#print(variavel1.pilha)

print(variavel1.empilhar("prato de porcelana"))
print(variavel1.empilhar("prato de vidro"))
print(variavel1.empilhar("prato de madeira"))
print(variavel1.empilhar("prato de metal"))
print(variavel1.empilhar("prato de plastico"))
print(variavel1.empilhar("prato de barro"))
print(variavel1.desempilhar())
print(variavel1.desempilhar())
print(variavel1.desempilhar())

# ---------------------------------------------------------------------------------------------------------------
# Encapsulamento 
# ---------------------------------------------------------------------------------------------------------------

# As variaveis com dois underline (__) agora nâo podem ser acessadas fora dessa classe, elas estão ocultas;

class Pilha: # classes começam com letra maiuscula 

    def __init__(self): # função que inicializa uma classe e adiciona caracteristicas a esse objeto Pilha 
        self.__pilha = list()
        self.__limite = 5
        self.__quantidade = 0 
    
    def empilhar(self, item):
        if self.__quantidade < self.__limite:
            self.__pilha.append(item)
            self.__quantidade += 1 
            return(f"{item} adicionado à pilha.")
        else:
            return(f"Essa pilha já tem {self.quantidade} items.")

    def desempilhar(self): 
        if self.__quantidade > 0: 
           del self.__pilha[-1]
           self.__quantidade -= 1
           return(f"Item removido.")
        else:
           return(f"A pilha ja está vazia!")

# Exemplo - vai dar erro: 
        
#pilha_de_roupas = Pilha()
#print(pilha_de_roupas.limite)

# -------------------------------------------------------------------------------
# Herança: classes que são subclasses de outra 
# -------------------------------------------------------------------------------

class Funcionario:

    def __init__(self):
       # self.nome = ""
        self.salario = 0
        self.idade = 0
    
#    def checa_nome(self):
#        return(self.nome)
        
    def seta_salario(self, salario):
        self.salario = salario

class Gerente(Funcionario):  # uma classe gerente subclasse da funcionario

    def __init__(self): 
        super().__init__() # todas caracteristicas do funcionario importadas
        #self.salario = self.salario * 1.5
        self.bonus = 1.3 

    def aplica_bonus(self):
        self.salario = self.salario * self.bonus

joao = Funcionario()
joao.seta_salario(2000)
print(joao.salario)

pedro = Gerente()
pedro.seta_salario(3000)
pedro.aplica_bonus() 
print(pedro.salario)

# -------------------------------------------------------------------------------
# Polimorfia/polimorfismo 
# alterar heranças de uma classe 
# -------------------------------------------------------------------------------

class Funcionario:

    def __init__(self):
        self.salario = 2500
        self.nome = ""
        self.idade = ""

    def define_salario(self, salario):
        self.salario = salario


class Gerente(Funcionario):

    def __init__(self):
        super().__init__()
        self.salario = self.salario * 1.3

# ======================================================================



