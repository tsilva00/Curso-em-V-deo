import random
p = str(input('Nome do primeiro aluno: '))
s = str(input('Nome do segundo aluno: '))
t = str(input('Nome do terceir aluno: '))
q = str(input('Nome do quarto aluno: '))
lista = [p, s, t, q]

escolhido = random.choice(lista)
print('O(A) aluno(a) escolhido(a) foi {}!'.format(escolhido))