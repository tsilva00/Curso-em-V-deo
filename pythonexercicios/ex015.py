km = float(input('Quantos km você percorreu?'))
d = int(input('O carro está alugado por quantos dias?'))

gas = km*0.15
dias = d*60
total = gas + dias

print('Levando em consideração que você gastou R${:.1f} de gasolina e R${} de aluguel, o gasto total foi de {:.2f}'.format(gas, dias,total))
