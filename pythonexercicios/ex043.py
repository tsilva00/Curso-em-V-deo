p = float(input('Digite o seu peso:'))
a = float(input('Digite a sua altura: '))
IMC = p/(a**2)


print('O seu IMC é igual a {:.1f}! Você está '.format(IMC), end='')
if IMC <= 18.5:
    print('abaixo do peso!')
elif 18.5 < IMC <25:
    print('no peso ideal!')
elif 25 < IMC < 30:
    print('sobrepeso!')
elif 30<IMC<40:
    print('com obesidade!')
elif IMC>40:
    print('com obesidade mórbida!')