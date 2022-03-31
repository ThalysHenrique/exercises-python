""" Ex p/ somar duas notas do aluno e calcular a média"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Somando a nota {:.1f} e nota {:.1f}, a média é {:.1f}'.format(nota1, nota2, média))