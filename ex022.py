""" Exercício p/ mostrar nome com todas as letras maiúsculas e minúsculas

    Quantas letras ao todo (sem considerar o espaço)

    Quantas letras tem o primeiro nome
 """

frase = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(frase.upper()))
print('Seu nome em minúsculas é {}'.format(frase.lower()))
print('Seu nome ao todo tem {}'.format(len(frase) - frase.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))
separa = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))