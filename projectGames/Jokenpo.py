#PEDRA, PAPEL OU TESOURA
import random

print('ESCOLHA!')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('Não me deixe roubar, digite o objeto escolhido!')
esc = input('R:').capitalize().strip()
lista = ['Pedra', 'Papel', 'Tesoura']
sort = random.choice(lista)
print('Eu escolhi...', sort)
if esc == 'Papel' and sort == 'Pedra':       #PAPEL GANHA PEDRA
    print('Você ganhou :,)')
elif esc == 'Tesoura' and sort == 'Papel':    #TESOURA GANHA PAPEL
    print('Você ganhou :,)')
elif esc == 'Pedra' and sort == 'Tesoura':     #PEDRA GANHA TESOURA
    print('Você ganhou :,)')
elif esc == sort:
    print('Empatamos :)')
else:
    print('Eu ganhei! :p')
