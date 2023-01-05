print('Js Viagens')
km = int(input('Digite a distância da viagem:'))
if km >= 200:
    prec = 0.45 * km
    print('O valor a ser pago é de', prec)
else:
    prec1 = 0.50 * km
    print('O valor a ser pago é de', prec1)
