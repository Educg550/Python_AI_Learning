# -*- coding: utf-8 -*-
num = int(input("Digite um número para gerar a sua tabuada: "))

for i in range (1, 11):
    print("{} X {} = {}".format(num, i, num * i))