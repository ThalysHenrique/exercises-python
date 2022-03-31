""" Exercício p/ informar quantos litros de tinta é preciso para pintar uma parede de determinada largura x altura"""

largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area = largura * altura
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar sua parede, você precisará de {} litros de tinta'.format(tinta, area))