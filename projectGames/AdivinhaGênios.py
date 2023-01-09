import random

print('-=+=-' * 11)
print('                     AdivGênios                    ')
print(' ')
print('COMO JOGAR: O gênios vai pensar em número de 0 a 20')
print('tente adivinhar :) ')
print('-=+=-' * 11)
print(' ')
print(' ')
nome = input('Digite seu nome para participar:').strip()
print('Boa sorte e divirta-se,',nome)

print(' ')
print(' ')
print('_____________________________________')
print('       ESCOLHENDO EM UM NÚMERO')
print('_____________________________________')
print(' ')
print(' ')

x = random.randint(0, 5)
num = int(input('Em que número pensei:'))
if num == x:
    print('Você acertou!')
else:
    print('Você errou;-;')
    print('O número escolhido foi:', x)
    print('Resete o sistema e tente novamente.')
