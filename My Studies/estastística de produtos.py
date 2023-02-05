import time
soma = 0
maiorprec = 0
menorprec= 10
ol = 0
resposta = 'S'
while resposta != "N":
    prod = str(input('Nome do produto:'))
    prec = int(input('Preço:'))
    resposta = input('Deseja continuar:[S/N] ').capitalize().strip()
    time.sleep(1)
    soma += prec
    if prec > maiorprec:
        maiorprec = prec
    if prec < menorprec:
        menorprec = prec
    time.sleep(1)
print(f'Foi gastado {soma} reais em produtos')
print(f'O maior valor é {maiorprec}')
print(f'O menor valor é {menorprec}')
