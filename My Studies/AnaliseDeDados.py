base = []
pessoas = []
dados = []
contar_pessoas = 0

while True:
    base.append(str(input('Digite seu nome: ')))
    base.append(float(input('Digite seu peso:')))
    pessoas.append(base[:])
    base.clear()
    resposta = input('Deseja continuar [S/N?] ')
    if resposta in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Os dados foram{pessoas}')