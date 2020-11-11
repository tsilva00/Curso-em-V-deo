a = float(input('Escreva o tamanho da primeira reta:'))
b = float(input('Escreva o tamanho da segunda reta:'))
c = float(input('Escreva o tamanho da terceira reta:'))

if (b-c)<a<b+c and (a-c)<b<a+c and (a-b)<c<a+b:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if a == b == c:
        print('equilátero!')
    elif a == b or a == c or c == b:
        print('isósceles!')
    elif a != b != c != a:
        print('escaleno!')
else:
    print('Não é possível formar um triângulo com esses segmentos!')