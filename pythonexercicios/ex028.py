from random import randint
from time import sleep
#Faz o programa escolher um número aleatório
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
print('PROCESSANDO...')
sleep(2)
#Faz o jogador escolher um número
num = int(input('Em que número eu pensei?'))
if computador == num:
    print('PARABÉNS, você conseguiu me vencer!!!')
else:
    print('VENCI! Eu pensei no número {} e não no número {}!'.format(computador, num))
