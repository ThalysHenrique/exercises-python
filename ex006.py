""" Ex p/ mostrar o dobro, triplo e a raiz quadrada de um número"""

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} vale {}. a raiz quadrada de {} vale {:.2f}'.format(n, t, n, r))