nome = input('Esreva seu nome completo:')
mai = nome.upper()
min = nome.lower()
num = len(nome) - nome.count(' ')
div = nome.split()
p = len(div[0])

#O que vai ser impresso
print('Analisando seu nome...')
print('O seu nome em maiúsculo é {}'.format(mai))
print('O seu nome em minúsculo é {}'.format(min))
print('O seu nome tem {} letras'.format(num))
print('Seu primeiro nome {} tem {} letras'.format(div[0], p))