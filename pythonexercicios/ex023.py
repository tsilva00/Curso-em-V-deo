num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))

if num >= 0 and num <=9999:
          print('Unidade: {}'.format(u))
          print('Dezena: {}'.format(d))
          print('Centena: {}'.format(c))
          print('Milhar: {}'.format(m))
else:
          print('O número inserido é inválido!')



