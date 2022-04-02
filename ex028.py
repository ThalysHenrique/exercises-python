""" Exercício para montar um game em que o jogador tem que adivinhar o número que o computador pensou """

from msilib.schema import Component
from random import randint
from time import sleep
computer = randint(0, 5) #faz o computador pensar
print('=-=' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('=-=' * 20)
player = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1)
if player == computer:
    print('Você venceu, PARABÉNS!')
else:
    print('Pensei no número {} e não {}, tente outra vez!'.format(computer, player))