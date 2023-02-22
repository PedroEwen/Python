print('[-------------------]')
print('|Descontão da galera|')
print('[-------------------]')
valori = float(input('Valor original:'))
desc = float(input('Desconto:'))
calc = (desc/100) * valori
valf = valori - calc
print('O valor a pagar será de', valf)
