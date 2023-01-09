print('Digite o lados do triângulo')
a = int(input('Lado 1:'))
b = int(input('Lado 2:'))
c = int(input('Lado 3:'))

if a + b > c or a + c > b or b + c > a:
    print('Formar um triãngulo')
else:
    print('Não formará um triângulo')
