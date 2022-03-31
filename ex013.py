""" Exercício p/ informar valor do novo salário do desenvolvedor com 15% de aumento"""

salarioatual = float(input('Valor do salário atual: R$'))
reajuste = salarioatual + (salarioatual * 15 / 100)
print('O salário atual do desenvolvedor python é R${} e com o reajuste de 15% ficará R${}'.format(salarioatual, reajuste))