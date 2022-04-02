""" name = str(input('Whats your name? '))
if name == 'Thalys':
    print('Your name is very beautiful!')
else:
    print('Good morning', name, '!') """


n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print(m, 'Sua média foi boa, parabéns!')
else:
    print(m, 'Sua média não foi boa, estude mais!')