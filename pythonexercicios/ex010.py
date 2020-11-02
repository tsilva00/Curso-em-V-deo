real = float(input('Quantos reais você tem:'))

conv = (real/3.27)

print('Levando em consideração que o dólar está US$3.27, com {} reais você pode comprar {:.2f} dólares!'.format(real, conv))