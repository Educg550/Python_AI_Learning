# -*- coding: utf-8 -*-
def somatorio(* values): # parâmetro é recebido como Tuple
    """
    -> Função que recebe n números e retorna o somatório deles
    :param * values: números a serem somados
    """
    res = 0
    for v in values:
        res += v
    return res
def produtorio(* values): # parâmetro é recebido como Tuple
    """
    -> Função que recebe n números e retorna o produtório deles
    :param * values: números a serem multiplicados
    """
    res = 1
    for v in values:
        res *= v
    return res

tupla = (int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")))
# Operador * expande a tupla dentro dos argumentos
print(f'O somatório dos números é {somatorio(* tupla)}')
print(f'O produtório dos números é {produtorio(* tupla)}')