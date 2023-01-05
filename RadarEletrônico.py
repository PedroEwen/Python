print('             RADAR ELETRÔNICO - PRF         ')
print(' _'* 25)
vel = int(input('           Qual a sua velocidade atual:'))
km = vel - 80
multa = km * 7
if vel > 80:
    print('     Você foi multado por exeder o limite permitido!')
    print('     O valor da multa será  de:', multa, 'reais')
else:
    print('     Parabéns, está dentro do limite permitido!')
