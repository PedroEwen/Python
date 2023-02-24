from ntpath import join
import random
import time

print('Gerador de Senhas fortes')

minu = 'abcdefghijklmnopqrstuvwxyz'
mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
sim = '!@#$%¨&*(){}[]?><.</|'

tmh_senha = int(input('Digite o tamanho da sua senha: '))
print('processando.')
time.sleep(1)
print('processando..')
time.sleep(1)
print('processando...')
tudo = minu + mai + num + sim
senha_forte = ''.join(random.sample(tudo, tmh_senha))
time.sleep(1)
print(f'Senha criada: {senha_forte}')
