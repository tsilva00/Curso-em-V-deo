d = float(input('Qual a distância da sua viagem? '))
if d <= 200:
    print('O preço da sua viagem é R${:.2f}'.format(d*0.50))
else:
    print('O preço da sua viagem é R${:.2f}'.format(d*0.45))