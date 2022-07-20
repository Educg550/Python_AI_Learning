# -*- coding: utf-8 -*-
from random import randint
from operator import itemgetter
jogadores = list()
resultados = list()
jogador = dict()
for i in range(1, 5):
    jogador['nome'] = str(input("Digite o nome do jogador {}: ".format(i)))
    jogador['resultado'] = randint(1, 6)
    jogadores.append(jogador.copy())
    jogador.clear()
jogadores = sorted(jogadores, key=itemgetter('resultado'), reverse = True)
for p in jogadores:
    print(f"{p['nome']} tirou {p['resultado']} no dado")
