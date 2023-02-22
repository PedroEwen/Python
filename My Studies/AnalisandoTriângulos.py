l1 = int(input('Digite o primeiro lado:'))
l2 = int(input('Digie o segundo lado:'))
l3 = int(input('Por fim, o último lado:'))
if l1 == l2 == l3:
    print('Triângulo equilátero')
elif l1 != l2 != l3:
    print('Triângulo escaleno')
else:
    print('Triângulo isósceles')
