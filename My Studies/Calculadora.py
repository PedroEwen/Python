import time
r = 0
print('CALCULADORA UNIVERSAL')
num = int(input('Valor 1:'))
ndois = int(input('Valor 2:'))
time.sleep(1)
while r != 7:
    time.sleep(2)
    print('\033[0:30m---Menu---\033[m')
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplição')
    print('[4] Divisão')
    print('[5] Raiz quadrada')
    print('[6] Novos números')
    print('[7] Sair do programa')
    r = int(input('Selecione a opção conforme o número:'))
    if r == 1:
        resultado = num + ndois
        print(f'A soma de {num} + {ndois} = {resultado}')
    elif r == 2:
        resultado = num - ndois
        print(f'A subtração de {num} - {ndois} = {resultado}')
    elif r == 3:
        resultado = num * ndois
        print(f'A multiplicação de {num} x {ndois} = {resultado}')
    elif r == 4:
        resultado = num / ndois
        print(f'A Divisão de {num} / {ndois} = {resultado}')
    elif r == 5:
        resultado = (num + ndois) / 2
        print(f'A raiz quadradada {num} + {ndois} = {resultado}')
    while r == 6:
        print('Digite os novos números')
        num = int(input('Valor 1:'))
        ndois = int(input('Valor 2:'))
        print('[1] Somar')
        print('[2] Subtrair')
        print('[3] Multiplição')
        print('[4] Divisão')
        print('[5] Raiz quadrada')
        print('[6] Novos números')
        print('[7] Sair do programa')
        r = int(input('Selecione a opção conforme o número:'))
        if r == 1:
            resultado = num + ndois
            print(f'A soma de {num} + {ndois} = {resultado}')
        elif r == 2:
            resultado = num - ndois
            print(f'A subtração de {num} - {ndois} = {resultado}')
        elif r == 3:
            resultado = num * ndois
            print(f'A multiplicação de {num} x {ndois} = {resultado}')
        elif r == 4:
            resultado = num / ndois
            print(f'A Divisão de {num} / {ndois} = {resultado}')
        elif r == 5:
            resultado = (num + ndois) / 2
            print(f'A raiz quadradada {num} + {ndois} = {resultado}')
print('Obrigado por utilizar a calculadora universal')
