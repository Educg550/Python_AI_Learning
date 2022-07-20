# -*- coding: utf-8 -*-
tupla = (int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")))
print(f'Você digitou os valores {tupla}')
pares = ()
for n in tupla:
    vezes = 0
    for i in range(0, len(tupla)):
        if tupla[i] == n:
            vezes += 1
    print(f'O valor {n} apareceu {vezes} vezes')
    if not bool(n % 2):
        pares = pares + (n,)
print(f'Os valores pares digitados foram {pares}')