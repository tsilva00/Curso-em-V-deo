cidade = str(input('Em que cidade você nasceu?'))
mai = cidade.upper()

if mai[:5] == 'SANTO':
    print('True')
else:
    print('False')

#Outra alternativa
#cid = str(input('Em que cidade você nasceu?'))
#print(cid[:5].upper() == 'SANTO')