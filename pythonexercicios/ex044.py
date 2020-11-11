v = float(input('Digite o valor do produto: '))
p = input('Formas de pagamento:\n[1]À vista no Dinheiro/Cheque\n[2]À vista no cartão\n[3]No cartão, até 2x sem juros\n[4]No cartão, 3X ou mais com juros\nQual vai ser a forma de pagamento escolhida?')

if p == '1':
    a = v*0.1
    v1 = v - a
    print('Você vai pagar R${:.2f} no produto'.format(v1))
elif p == '2':
    b = v*0.05
    v2 = v - b
    print('Você vai pagar R${:.2f} no produto'.format(v2))
elif p == '3':
    print('Você vai pagar R${:.2f} no produto'.format(v))
else:
    c = v*0.20
    v3 = v + c
    print('Você vai pagar R${} no produto'.format(v3))