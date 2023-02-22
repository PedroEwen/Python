
nums = []
r = 's'
while r == 's':
    num = int(input('Digite um valor:'))
    r = str(input('Deseja continuar: [s/n]?'))
    if r == 'Nn':
        break
    nums.append(num)
    nums.sort(reverse=True)
print(f'Você digitou {len(nums)} valores')
print(f'São eles: {nums}')
if 10 in nums:
    print('O valor 10 faz parte dos elementos')
