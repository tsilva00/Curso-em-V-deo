sal = float(input('Qual o seu salário? '))
if sal <= 1250.00:
    print('Você vai receber um aumento de R${:.2f}'.format(sal*0.10))
else:
    print('Você vai receber um aumento de R${:.2f}'.format(sal*0.15))
