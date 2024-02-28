# 1) Crie uma classe que represente um ônibus. O ônibus deverá conter os seguintes atributos:

# capacidade total
# capacidade atual
# movimento

# Os comportamentos esperados para um Ônibus são:
# Embarcar
# Desembarcar
# Acelerar
# Frear

# Lembre-se que a capacidade total do ônibus é de 45 pessoas - não será possível admitir super-
# lotação. Além disso, quando o ônibus ficar vazio, não será permitido efetuar o desembarque
# de pessoas. Além disso, pessoas não podem embarcar ou desembarcar com o onibus em movimento.
import os, time

def limpa_tela():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

class Bus:
    def __init__(self):
        self.cap_total = 45
        self.cap_atual = 0 
        self.velocidade = 0 
        
    def checa_bus(self):
        limpa_tela()
        print(f"Velocidade do ônibus: {self.velocidade} km/h.")
        print(f"Número de passageiros: {self.cap_atual}")
        time.sleep(3)

    def acelera(self):
        limpa_tela()
        self.velocidade += 10 
        print(f"A velocidade do ônibus agora é de {self.velocidade}km por hora.")
        #return self.velocidade
        time.sleep(3)

    def frear(self):
        limpa_tela()
        if self.velocidade == 0:
            print("Onibus está parado.")
        else:
            self.velocidade -= 10 
            print(f"A velocidade do ônibus agora é de {self.velocidade}km por hora.")
            #return self.velocidade
        time.sleep(3)

    def embarca(self, passageiros):
        limpa_tela()
        if self.velocidade > 0: 
            print("O onibus ainda está em movimento!")
        else:
            if self.cap_atual == self.cap_total:
                print("Capacidade máxima excedida! Aguarde o próximo.")
            else:
                self.cap_atual = self.cap_atual + passageiros
                print("Passageiro embarcado!")
                print(f"Nova lotação é de {self.cap_atual} passageiros.")
        time.sleep(3)


    def desembarca(self, passageiros): 
        limpa_tela()
        if self.velocidade > 0:
            print("O onibus ainda está em movimento!")
        else:
            if self.cap_atual == 0:
                print("Onibus está vazio.")
            else:
                self.cap_atual = self.cap_atual - passageiros 
                print("Passageiro desembarcado!")
                print(f"Nova lotação é de {self.cap_atual} passageiros.")
        time.sleep(3)


# variaveis 
#cap_atual = 0 
#velocidade = 0
passageiros = 46

# instanciando bus
busao = Bus()

# testing
#velocidade = busao.acelera(velocidade)
#print(velocidade)
#velocidade = busao.frear(velocidade)
#print(velocidade)
#busao.embarca(passageiros)
#busao.checa_bus()
#busao.desembarca(passageiros)
#busao.checa_bus()


# inicio da rotina

while True:

    limpa_tela()
    print(40*"-")
    print("Bem vindo à linha 2.12 de transporte publico!")
    print(40*"-")
    resposta = input("""
    Selecione uma opção para simular o ônibus:
                     
    0 - Sair do programa
    1 - Dados atuais do ônibus
    2 - Embarcar passageiros
    3 - Desembarcar 1 passageiro
    4 - Acelerar o ônibus
    5 - Frear o ônibus
                     
    Digite aqui sua opção: """)

    if resposta == "0":
        print("Saindo do programa, até mais!")
        break

    if resposta == "1":
        busao.checa_bus()

    if resposta == "2": 
        busao.embarca(passageiros)

    if resposta == "3":
        busao.desembarca(passageiros)

    if resposta == "4": 
        busao.acelera() 

    if resposta == "5":
        busao.frear()
