# -*- coding: utf-8 -*-
num = int(input("Digite a n-ésima posição da sequência de Fibonacci: "))
fibo = [0, 1]

for i in range(2, num + 1):
    fibo.append(fibo[i - 2] + fibo[i - 1])
print("O {}-ésimo termo de Fibonacci é {}".format(num, fibo[num]))