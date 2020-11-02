import math

an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
cosc = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('O ângulo {} tem o SENO de {:.2f}!'.format(an, seno))
print('O ângulo {} tem o COSSENO de {:.2f}!'.format(an, cosc))
print('O ângulo {} tem a TANGENTE de {:.2f}!'.format(an, tan))