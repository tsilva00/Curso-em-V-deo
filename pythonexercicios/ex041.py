a = int(input('Digite o ano em que você nasceu: '))
c = 2020-a

if c <=9:
    print('MIRIM')
elif 10 <= c <= 14:
    print('INFANTIL')
elif 15 <= c <= 19:
    print('JUNIOR')
elif c == 20:
    print('SêNIOR')
elif c >= 21:
    print('MASTER')