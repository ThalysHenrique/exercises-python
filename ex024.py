""" Exercício para ler um nome e dizer se a cidade começa com a palavra santo """

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper == 'SANTO')