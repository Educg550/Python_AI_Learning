# -*- coding: utf-8 -*-
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez')
while True:
    num = int(input("Digite um número entre 0 e 10: "))
    if num >= 0 and num <= 10:
        print(cont[num])
    else:
        break