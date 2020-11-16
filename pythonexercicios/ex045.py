import random

j = ['Pedra', 'Papel', 'Tesoura']

e = random.choice(j)
jogo = input('Olá!!! Vamos jogar um jogo de Jokenpô, espero que esteja pronto!\nPedra, Papel ou Tesoura...\nQual a sua escolha? ')

if jogo == 'Pedra' and e == 'Tesoura'  or jogo == 'Papel' and e == 'Pedra' or jogo == 'Tesoura' and e == 'Papel':
    print('Eu escolhi {}, então você ganhou!!!'.format(e))
elif jogo == e:
    print('Eu escolhi {}, então foi empate!'.format(e))
else:
    print('Eu escolhi {}, então eu ganhei!!!'.format(e))