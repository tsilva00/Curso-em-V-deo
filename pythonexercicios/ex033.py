a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
menor = a
#Verificando quem é menor:
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior
maior = c
if b>c and b > a:
    maior = b
if a > c and a > b:
    maior = a

print('O maior valor digitado foi {} e o menor foi {}!'.format(maior, menor))