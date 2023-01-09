#PEDRA, PAPEL OU TESOURA
import time
import random

print('ESCOLHA:')
print('- Pedra')
print('- Papel')
print('- Tesoura')
print('Não me deixe roubar, digite o objeto escolhido!')
esc = input('R:').capitalize().strip()
time.sleep(1)
lista = ['Pedra', 'Papel', 'Tesoura']
sort = random.choice(lista)
print('Eu escolhi...')
time.sleep(1)
if esc == 'Papel' and sort == 'Pedra':       #PAPEL GANHA PEDRA
    print(sort+', você ganhou :,)')
elif esc == 'Tesoura' and sort == 'Papel':    #TESOURA GANHA PAPEL
    print(sort+', você ganhou :,)')
elif esc == 'Pedra' and sort == 'Tesoura':     #PEDRA GANHA TESOURA
    print(sort+', você ganhou :,)')
elif esc == sort:
    print(sort+', empatamos :)')
else:
    print(sort+', eu ganhei')
