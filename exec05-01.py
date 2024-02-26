# 1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
# deverá ser apresentado vencedor.

# Dica: [OPCIONAL] Você poderá utilizar o modulo "time" para simular um tempo de a cada rodada para criar
# um efeito mais interessante.

# Dica: [OPCIONAL] Tentem fazer a remoção de uma pessoa aleatória por rodada sem utilizar a função "choice".

import random, time 
print(40*"-")
print("Que comecem os jogos! :) ")
print(40*"-")
participantes = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", "Rosangela", "Rian"]
# INDEX             0       1        2         3          4         5        6        7           8          9

for rodada in range (1,10):
    eliminado = participantes[random.randint(0, len(participantes) -1)]
    print(f"Na {rodada}ª rodada, {eliminado} foi eliminado(a)")
    participantes.remove(eliminado)
    print("Começando próxima rodada...")
    time.sleep(2)

print(f"No fim, {participantes[0]} foi o vencedor!")