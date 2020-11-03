a = float(input('Escreva o tamanho da primeira reta:'))
b = float(input('Escreva o tamanho da segunda reta:'))
c = float(input('Escreva o tamanho da terceira reta:'))

if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
    print('É possível construir um triângulo!')
else:
    print('Nã é possícel construir um triângulo!')