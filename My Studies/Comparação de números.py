num = int(input('Digite o primeiro valor:'))
ndois = int(input('Digite o segundo valor:'))
if num > ndois:
    print(num, 'é maior que', ndois)
elif ndois > num:
    print(ndois, 'é maior que', num)
else:
    print('Eles são iguais!')
