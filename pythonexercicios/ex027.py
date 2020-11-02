nome = str(input('Escreva seu nome completo:'))
p = nome.split()


print('O seu primeiro nome é {}'.format(p[0]))
print('O seu último nome é {}'.format(p[len(p)-1]))