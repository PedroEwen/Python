import time 
print('         Locadora Ewen')
print('     Os melhores filmes estão aqui')
print('1 - Cadastrar filmes')
print('2 - Ver catálogo')
print('0 - Sair')
r = int(input('Selecione uma opção: '))
catalogo = ['Nemo', 'Dory', 'Jumanji'] #Catálogo
while r == 1:                                                           # r e r2 == resposta do usuário
        filme = str(input("Adicione um filme ao catálogo:"))
        if filme != ' ':
            catalogo.append(filme)                          #Adição de filmes ao catálogo
            print('Filme adiconado com sucesso')
            r2 = input('Deseja ver o catálogo?')
            if r2 == 'sim'or r2 == 'Sim':
                print('Catálogo de Filmes ')
                print(catalogo)
                break
if r == 2:
    print('O catálogo atualizado de filmes da locadora')
    print(catalogo)
elif r == 0: 
     print('Obrigado e volte sempre')

