valor = float(input('Valor do produto:'))
print(' - Dinheiro')
print(' - Débito')
print(' - Parcelamento ')
pagamento = input('COMO DESEJA PAGAR:').capitalize().strip()
if pagamento == 'Dinheiro':
    novovalor = valor - (valor * 0.1)
    print('Você terá 10% de desconto no pagamento em dinheiro!')
    print('O novo valor será de', novovalor, 'reais')
elif pagamento == 'Débito':
    novovalor = valor - (valor * 0.05)
    print('Você terá um desconto no débito')
    print('o novo valor será de', novovalor, 'reais')
elif pagamento == 'Parcelamento':
    print('2x - Sem juros')
    print('3x - com juros')  # 5%
    print('4x - com juros')  # 7%
    print('5x - com juros')  # 10%
    vzs = str(input('Em quantas vezes: '))
    if vzs == '2x':
        print('Valor será de', valor, 'reais divididos em 2x')
    elif vzs == '3x':
        novovalor = valor + (valor * 0.05)
        print('Valor será de', novovalor, 'reais divididos em 3x')
    elif vzs == '4x':
        novovalor = valor + (valor * 0.07)
        print('Valor será de', novovalor, 'reais dividos em 4x')
    elif vzs == '5x':
        novovalor = valor + (valor * 0.1)
        print('Valor será de', novovalor, 'reais dividos em 5x')
    else:
        print('Não temos essa opção de parcelamento')
