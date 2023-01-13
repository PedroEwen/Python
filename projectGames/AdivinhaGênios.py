import random
import time

print('-' * 20)
print('   \033[7mAdivinhos V2.0\033[m')
print('-' * 20)
print('')
nome = input('Insira o nome do participante:').capitalize()
while nome == ' ':
    print('\033[0:31mNome inválido\033[m')
    nome = input('Insira o nome do participante:').capitalize().strip()
print(f'\033[0:35mDivirta-se\033[m, {nome}')
print('\033[4:36mRegras\033[m'':')
time.sleep(2)
print('\033[0:34mO computador irá escolher de 0 a 5;\033[m')
print('\033[0:34mO computador irá escolher um número aleatoriamente e você deverá acertar!\033[m')
time.sleep(2)
print('\033[0:35mO jogo está sendo iniciado\033[m!')
print('-' * 25)
print(' \033[0:37mComputador escolhendo...\033[m')
print('-' * 25)
sort = random.randint(0, 5)
num = int(input('\033[0:37mEm número eu pensei:\033[m'))
while num > 5 or num < 0:
    print('\033[0:31mLembre-se que é de 1 a 5 :), Tente outro:\033[m')
    num = int(input('\033[0:37mEm que número eu pensei:'))
if num == sort:
    time.sleep(2)
    print('\033[0:32mVocê acertou o número sorteado!\033[m')
else:
    time.sleep(2)
    print(f'\033[0:31mNão foi dessa vez\033[m, o número sorteado foi \033[0:33m{sort}\033[0:33m')
