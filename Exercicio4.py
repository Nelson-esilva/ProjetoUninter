#Boas vindas e informações da loja
print('Bem-vindo ao Controle de livros do Nelson Emeliano Silva')
simbolo = '*' * 60
print(simbolo)

lista_livro = []
id_global = 0

#Função para realizar o cadastro dos livros na loja virtual
def cadastrar_livro(id):
    global lista_livro
    try:
        while True:
            print('-' * 21 + ' MENU DE CADASTRO ' + '-' * 21)
            id_livro = id
            print("Id do livro {}".format(id))
            nome = input('Por favor entre com o nome do livro: ')
            autor = input('Por favor entre com o autor: ')
            editora = input('Por favor entre com a editora: ')
            if (nome and autor and editora):                                     #Testa se a entrada foi vazia em algum dos itens
                break
            else:
                print('Você não forneceu uma entrada válida. Tente novamente.\n ')
                continue
    except ValueError:      #Testa se a entrada foi caractere no campo ID.
        print('Opção inválida. Tente novamente.\n ')
    dados_livro = {'id':id_livro,'nome':nome,'autor':autor,'editora':editora}   #Cria um dicionario com os dados do livro.
    lista_livro.append(dados_livro)                                             #Adiciona o dicionário criado a uma lista global.
    print('*' * 60)

#Função para realizar a consulta dos livros na loja virtual
def consultar_livro():
    while True:
        try:
            print('*' * 60)
            print('-' * 21 + ' MENU DE CONSULTA ' + '-' * 21)
            print('Escolha a opção desejada:')
            print('1 - Consultar todos os livros')
            print('2 - Consultar livro(s) por Id')
            print('3 - Consultar livro(s) por autor')
            print('4 - Retornar')
            print('*' * 60)
            x = int(input())
            if (x == 1 or x == 2 or x == 3 or x == 4):
                if (x == 1):                                                    #Consulta todos os livros cadastrados
                    for dicionario in lista_livro:
                        for chave, valor in dicionario.items():                 #Imprime a lista de livros na tela de forma ordenada.
                            print(f'{chave}: {valor}')
                        print()
                elif (x == 2):                                                  #Consulta os livros pelo ID
                    id_livro = int(input('Qual o ID do livro? '))
                    for i in range (1,len(lista_livro)+1,1):
                        if (id_livro == lista_livro[i-1]['id']):
                            for chave, valor in lista_livro[i-1].items():
                                print(f'{chave}: {valor}')
                            print()
                elif (x == 3):                                                  #Consulta os livros pelo autor
                    autor_livro = input('Qual o autor do livro? ')
                    for i in range (1, len(lista_livro)+1, 1):
                        if (autor_livro == lista_livro[i-1]['autor']):
                            for chave, valor in lista_livro[i - 1].items():
                                print(f'{chave}: {valor}')
                            print()
                else:                                                           #Retorna ao menu principal
                    break
            else:
                print('Entrada inválida. Tente novamente.')
        except ValueError:                                                      #Testa se a entrada fornecida foi caractere e solicita nova entrada.
            print('Entrada inválida. Tente novamente')
            continue

#Função para remover o livro da lista pelo ID
def remover_livro():
    try:
        print('-' * 21 + ' MENU REMOVER LIVRO ' + '-' * 21)
        id_remove = int(input('Digite o ID do livro a ser removido: '))
        for i in range (1, len(lista_livro)+1, 1):
            if ((lista_livro[i-1]['id']) == id_remove):
                item = lista_livro.pop(i-1)                                     #Remove da lista o item fornecido pelo usuário.
                lista_livro.append(item)                                        #Adiciona o item retirado para o fim da lista.
        lista_livro.pop()                                                       #Remove op ultimo item da lista.
        print('Removido com sucesso. Há {} livros restantes.\n '.format(len(lista_livro)))
            print()
    except ValueError:                                                          #Testa se a entrada fornecida foi caractere e solicita nova entrada.
        print('Opção Inválida. Tente novamente.')
    print('*' * 60)

#Programa Principal
while True:
    print('-' * 22 + ' MENU PRINCIPAL ' + '-' * 22)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    print('*' * 60)
    try:
        x = int(input())
        if (x == 1 or x == 2 or x == 3 or x == 4):
            if (x == 4):
                print('Encerrando programa. Obrigado.')
                break
            elif (x == 1):
                id_global = id_global + 1
                cadastrar_livro(id_global)
            elif (x == 2):
                consultar_livro()
            else:
                remover_livro()
        else:
            print('Opção Inválida. Tente Novamente.')
    except ValueError:                                                          #Testa se a entrada fornecida foi caractere e solicita nova entrada.
        print('Opção Inválida. Tente Novamente.')
