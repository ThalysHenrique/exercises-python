""" Exercício para calcular um ângulo qualquer e mostrar o valor do seno, cosseno e tangente desse ângulo """

from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = radians(ângulo)
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

