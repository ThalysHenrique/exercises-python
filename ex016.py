""" Exercício para mostrar porção inteira de um número quebrado """

from math import trunc
num = float(input('Digite um número: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

""" Outras maneiras de fazer 

    import math --> math.trunc(num)
    int(num)
"""