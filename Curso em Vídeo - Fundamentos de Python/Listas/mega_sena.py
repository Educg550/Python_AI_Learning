# -*- coding: utf-8 -*-
from random import randint
from time import sleep

print("MEGA-SENA")
print("=-" * 24, end = "")
print("=-=")
num = int(input("Digite o número de jogos que você deseja gerar: "))
lista = []
jogos = []
for i in range(0, num):
    for j in range(0, 6):
        random_num = randint(1, 60)
        while random_num in lista:
            random_num = randint(1, 60)
        lista.append(random_num)
    lista.sort()
    jogos.append(lista[:]) # copia somente o conteúdo à lista de jogos
    lista.clear()
for i in range(0, num):
    print(f"Jogo {i + 1}: {jogos[i]}")
    sleep(0.75)
print("=-" * 24, end = "")
print("=-=")
print(f"{num} jogos foram gerados. Boa sorte! 🍀")