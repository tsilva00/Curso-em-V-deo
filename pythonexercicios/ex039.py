nome = input('Digite seu nome: ')
a = int(input('Digite o ano em que você nasceu: '))
#Para ver se a idade do menino equivale a 18 anos
v = 2020-a
#Para ver quanto tempo falta ou passou para fulano se alistar
f = 18 - v
p = v - 18

if v == 18:
    print('{}, já está no momento de você se alistar ao serviço militar!'.format(nome))
elif v < 18:
    print('{}, ainda não está na hora de se alistar ao serviço militar, ainda falta(m) {} ano(s)!'.format(nome, f))
elif v> 18:
    print('{}, você deveria ter se alistado há {} ano(s) atrás, já passou do tempo!'.format(nome, p))