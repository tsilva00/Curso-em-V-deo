a = float(input('Qual a altura da parede:'))
l = float(input('Qual a largua da parede:'))

area = a*l
tinta = area/2

print('A área medida equivale a {}!\nVocê  vai precisar de {:.1f} latas de tinta'.format(area, tinta))