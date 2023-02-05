import random
import time
import random
cont = 0
resposta = 'S'
while resposta != 'N':
    time.sleep(1)
    print('_'*15)
    print('PAR OU ÍMPAR')
    print('_' * 15)
    num = int(input('Digite um valor:'))
    opc = str(input('PAR OU ÍMPAR:')).lower().strip()
    print('COMPUTADOR ESCOLHENDO!')
    time.sleep(2)
    sort = random.randint(0,5)
    calc1 = num + sort
    calc = (num + sort)%2
    if calc == 0:
        sis = 'par'
    elif calc != 0:
        sis = 'ímpar'
    if opc == sis:
        cont += 1
        time.sleep(1)
        print(f'Você ganhou, o número foi {sort} + {num} = {calc1}')
    elif opc != sis:
        print(f'Você perdeu, o número foi {sort} + {num} = {calc1}')
        print(f'A sequência de vitórias foi de {cont} vitórias')
        break
time.sleep(1)
print('Obrigado por jogar!')
