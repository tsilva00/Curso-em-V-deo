v = int(input('Qual a velocidade do seu carro?'))
m = (v - 80)*7

if v >= 80:
    print('Você está acima da velocidade permitida! O valor da sua multa é de R${:.2f}'.format(m))