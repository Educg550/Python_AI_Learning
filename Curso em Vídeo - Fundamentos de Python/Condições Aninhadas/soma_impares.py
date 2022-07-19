# -*- coding: utf-8 -*-
# Soma entre todos os números ímpares múltiplos de 3 
# que estão no intervalo de 1 até 500
s = 0

for i in range(3, 500, 3):
    if (bool(i % 2)):
        s += i
print("A soma de todos os valores solicitados é {}".format(s))