# -*- coding: utf-8 -*-
tuplinha = ('Lápis', 1.75,
            'Borracha', 0.5,
            'Caneta', 2.0,
            'Estojo', 25,
            'Régua', 5.75)
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
for i in range(0, 10):
    if not bool(i % 2):
        print(f'{tuplinha[i]:.<30}', end='')
    else:
        print(f'R${tuplinha[i]: >7.2f}')
print('-' * 40)
