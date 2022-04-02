""" Exercício p/ mostrar quantas vezes aparece a letra A, posição que ela aparece pela primeira vez e última vez """

nome = str(input('Informe seu nome: ')).upper().strip()
print('A letra A aparece {} vezes'.format(nome.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))