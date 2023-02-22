
par = []
impar =[]
numeros = []
r = 's'
while r != 'n': 
    numero = int(input('Digite um número: '))
    r = input('Deseja continuar: [S/N]?')
    if numero % 2 == 0:
        par.append(numero)
        numeros.append(numero)
    else:
        impar.append(numero)
        numeros.append(numero)
par.sort()
impar.sort()
numeros.sort()
print(f'Lista compelta: {numeros}')
print(f'Lista de pares: {par}')
print(f'Lista de ímpares: {impar}')
