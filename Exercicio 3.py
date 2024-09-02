#Boas vindas e informações da loja
print('Seja bem-vindo Copiadora do Nelson Emeliano Silva - RU:4666213')

#Selecionar o serviço com base na escolha do usuário.
#Testa as condições e retorna o valor do serviço.
def escolha_servico():
    while True:
        linha1 = 'DIG - Digitalização'
        linha2 = 'ICO - Impressão Colorida'
        linha3 = 'IBO - Impressão Preto e Branco'
        linha4 = 'FOT - Fotocópia'
        x = (input('Entre com o tipo de serviço desejado: \n{}\n{}\n{}\n{}\n'.format(linha1, linha2, linha3, linha4)))
        x = x.upper()
        if (x == 'DIG' or x == 'ICO' or x == 'IBO' or x == 'FOT'):
            if (x == 'DIG'):
                valor = 1.10
            elif (x == 'ICO'):
                valor = 1
            elif (x == 'IBO'):
                valor = 0.40
            else:
                valor = 0.20
            break
        else:
            print('Escolha inválida.\nEntre com o tipo de serviço novamente.\n')
    return valor

#Escolhe o número de páginas e testa se a entrada é valida ou não. Para ser válida deve ser um número inteiro.
#Retorna o valor das páginas com desconto.
def num_pagina():
    while True:
        try:
            x = int((input('Entre com o número de páginas desejada: ')))
            if (x > 0 and x < 20000):
                if (x <20):
                    desconto = x
                elif (x >= 20 and x < 200):
                    desconto = x - (x * 0.15)
                elif (x >= 200 and x < 2000):
                    desconto = x - (x * 0.20)
                else:
                    desconto = x - (x * 0.25)
                break
            else:
                print('Não aceitamos esse número de páginas. Por favor escolha um número entre 1 e 19.999')
        except:
            print('Entrada inváida. Por favor digite um número.\n')
    return desconto

#Função para escolher o número de páginas
#Testa se a entrada é válida ou nao e retorna o valor do adicional
def servico_extra():
    adicional = 0
    while True:
        try:
            linha1 = '1 - Encadernação Simples - R$15,00'
            linha2 = '2 - Encadernação Capa Dura - R$40,00'
            linha3 = '0 - Não desejo mais nada.'
            y = int(input('Deseja adicionar mais algum serviço?: \n{}\n{}\n{}\n'.format(linha1,linha2,linha3)))
            if (y == 1 or y ==2 or y ==0):
                if (y == 1):
                    adicional = 15
                elif (y == 2):
                    adicional = 40
                else:
                    break
                break
            else:
                print('Entrada inválida. Tente novamente.')
        except:
            print('Entrada inváida. Por favor digite um número.\n')
    return adicional

#Código principal que chama as funções e imprime na tela o valor final do serviço.
servico = escolha_servico()
pagina = num_pagina()
adicional = servico_extra()

total = servico * pagina + adicional
print('O valor total é: R${} (serviço: {} * paginas: {} + extra(s): {})'.format(total,servico,pagina,adicional))