# -*- coding: utf-8 -*-
import math

num = input("Digite um número: ")
if num == 1:
    eh_primo = False
else:
    eh_primo = True

for i in range(2, int(math.sqrt(num)) + 1):
    if (not bool(num % i)):
        eh_primo = False

if (eh_primo):
    print("{} é um número primo".format(num))
else:
    print("{} não é um número primo".format(num))