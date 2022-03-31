""" Exercício p/ informar novo preço do produto com desconto de 5%"""

preco = float(input('Qual o preço do produto?: R$'))
desconto = preco - (preco * 5 / 100)
print('O produto custava R${} e com desconto de 5% vai custar R${}'.format(preco, desconto))
