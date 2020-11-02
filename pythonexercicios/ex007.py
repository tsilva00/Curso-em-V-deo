nome = input('Qual o nome do(a) aluno(a)?')
nota1 = float(input('Escreva a primeira nota:'))
nota2 = float(input('Escreva a segunda nota:'))

media = (nota1+nota2)/2

print('A média de {} é igual a {:.2f}!'.format(nome, media))