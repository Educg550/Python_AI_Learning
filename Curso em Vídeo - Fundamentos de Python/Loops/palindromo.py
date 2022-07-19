# -*- coding: utf-8 -*-
frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.split()
frase = ''.join(frase)
invertido = ''
for i in range(len(frase) - 1, -1, -1):
    invertido = invertido + frase[i]
print("Normal: {} ".format(frase), "Invertido: {}".format(invertido))
if frase == invertido:
    print("A frase digitada é um palíndromo")
else:
    print("A frase digitada não é um palíndromo")