valorcasa = int(input('Insira o valor da casa:'))
salario = int(input('Insira seu sálario atual:'))
meses = int(input('Em quantos meses deseja pagar:'))
saldo = salario * 0.3   #30% do salario
pres = valorcasa / meses
if pres >= saldo:
    print('Empréstimo negado')
else:
    print('Empréstmo liberado')
