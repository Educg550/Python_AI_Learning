# -*- coding: utf-8 -*-
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input("Digite o valor de [{}][{}]: ".format(i, j))))
print("A matriz digitada é: ")
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(f"{matriz[i][j]} ", end = "")
    print("") # a função já pula linha por default