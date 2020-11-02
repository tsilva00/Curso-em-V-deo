co = int(input('Qual o comprimento do cateto oposto?'))
ca = int(input('Qual o comprimento do cateto adjascente?'))

h = ((co**2)+(ca**2))**(1/2)
print('O valor da hipotenusa desse triângulo é igual a {:.1f}'.format(h))
