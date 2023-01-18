sxm = 0
sxf = 0

for c in range(1, 5):
nome = input('Nome:')
idade = int(input('Idade:'))
sexo = input('Sexo:')
idade += idade
clc = idade / 4
if sexo == 'M':
sxm += 1
elif sexo == 'F':
sxf += 1
print('A média de idade do grupo é de', clc)
print('O grupo possui', sxf,'mulheres')
