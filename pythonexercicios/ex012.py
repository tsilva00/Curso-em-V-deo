valor = float(input('Qual o valor do produto?'))

perc = valor - (valor*0.05)

print('O valor a ser pago é de R${:.2f}!'.format(perc))