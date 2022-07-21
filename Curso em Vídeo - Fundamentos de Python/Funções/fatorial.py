# -*- coding: utf-8 -*-
def fatorial(num, show = False):
    """
    -> Calcula o fatorial de um número
    :param num: O número cujo fatorial deve ser calculado
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial + cálculo (a depender de show)
    """
    total = 1
    res = ""
    for i in range(0, num):
        if show:
            res = res + " {} ".format(num)
        if num > 1:
            if show:
                res = res + "x"
            total *= num
        elif show:
            res = res + "= {}".format(total)
            return res
        num -= 1
    return total
print(fatorial(10, True))