x = float(input('Digite o 1º número:'))
y = float(input('Digite o 2º número:'))
z = float(input('Digite o 3º número:'))

if x > y and x > z:
    print( x, 'é o maior número')
if x < y  and x < z:
    print('O menor número é', x)
if y > z and y > x:
    print(y, 'é o maior número')
if y < z and y < x:
    print('O menor número é', y)
if z > x and z > y:
    print(z, 'é o maior número')
if z < x and z < y:
    print('O menor número é', z)
