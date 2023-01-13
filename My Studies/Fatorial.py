import math
r = 1
n = int(input('Digite o valor do fatorial:'))
while n == 0:
print('Valor inválido!')
n = int(input('Digite o valor do fatorial:'))
print('O fatorial é', math.factorial(n))
