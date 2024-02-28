# ==========================================================================
# Implemente um programa que represente uma fila. O contexto do programa é uma
# agência de banco. Cada cliente ao chegar deverá respeitar a seguinte regra: o primeiro
# a chegar deverá ser o primeiro a sair. Você poderá representar pessoas na fila a par-
# tir de números os quais representam a idade. A sua fila deverá conter os seguintes
# comportamentos:

# • Adicionar pessoa na fila: adicionar uma pessoa na fila.
# • Atender Fila: atender a pessoa respeitando a ordem de chegada
# • Dar prioridade: colocar uma pessoa maior de 65 anos como o primeiro da fila

class Fila:

    def __init__(self):
        self.fila = []         # Fila
        self.prioridade = []   # Apenas um registro pra controle

    def adicionar(self, idade):
        if idade >= 65:
            self.prioridade.append(idade)
            self.fila.append(idade)
        else:
            self.fila.append(idade)
        
        return(f"Uma pessoa de {idade} anos se juntou à fila.")
    
    def atender(self):
        if len(self.fila) == 0:
            return("Não há ninguém na fila.")

        atendido = self.fila[0]
        if atendido in self.prioridade:
            self.prioridade.remove(atendido)

        self.fila.remove(atendido)
        return(f"Uma pessoa com {atendido} anos foi atendida.")
    
    def dar_prioridade(self):
        if len(self.prioridade) == 0:
            return("Não há ninguem acima de 65 anos na fila.")
        prioritario = self.prioridade[0]
        self.prioridade.remove(prioritario)
        self.fila.remove(prioritario)
        self.fila.insert(0, prioritario)

        return(f"Uma pessoa com {prioritario} anos recebeu prioridade e passou na frente.")
    

banco = Fila()

print(banco.adicionar(17))
print(banco.adicionar(25))
print(banco.adicionar(82))
print(banco.adicionar(56))
print(banco.adicionar(71))
print(banco.adicionar(36))

print(banco.atender())
print(banco.dar_prioridade())
print(banco.atender())
