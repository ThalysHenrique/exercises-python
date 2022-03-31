""" Aluguel de carros """

dias = int(input("Quantos dias alugados?: "))
km = float(input("Quantos KM foram percorridos?: "))
pago = (60 * dias) + (0.15 * km)
print('O valor total a ser pago é {:.2f}'.format(pago))