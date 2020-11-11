c = float(input('Qual o valor da casa que você quer comprar?'))
s = float(input('Qual o seu salário?'))
t = int(input('Em quantos anos você quer pagar?'))
prest = (c/t)/12
porc = s*0.3

if prest <= porc:
    print('Que ótimo, você vai conseguir comprar a casa pagando R${:.2f} por mês!'.format(prest))
else:
    print('Infelizmente você deveria comprar essa casa, já que a prestação de R${:.2f} equivale a mais do que 30% do seu salário!'.format(prest))
