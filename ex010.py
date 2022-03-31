""" Conversor de Moedas """

reais = int(input('Valor: '))
dc = reais / 4.76
print('Com R$ {} posso comprar {:.2f} dolares'.format(reais, dc))