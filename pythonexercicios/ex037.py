n = int(input('Digite um número decimal:'))
conv = input('Escolha em qual base numérica você quer converter: [1] Binário, [2] Octal ou [3] Hexadecimal:')

if conv == '1':
    b = bin(n)
    print('O número {} convertido para a base binária é {}'.format(n,b))
elif conv == '2':
    o = oct(n)
    print('O número {} convertido para a base octal é {}'.format(n,o))
elif conv == '3':
    h = hex(n)
    print('O número {} convertido para a base hexadecimal é {}'.format(n,h))