#Boas vindas e informações da loja
print('Seja bem-vindo a Loja de Gelados do Nelson Emeliano Silva - RU:4666213')
linha1 = '--------------------Cardápio----------------------'
linha2 = '------| Tamanho | Cupuaçu (CP) | Acaí (AC) |------'
linha3 = '------|    P    |   R$  9,00   |  R$ 11,00 |------'
linha4 = '------|    M    |   R$ 14,00   |  R$ 16,00 |------'
linha5 = '------|    G    |   R$ 18,00   |  R$ 20,00 |------'
linha6 = '--------------------------------------------------'

#Imprime infomações da loja na tela
print('{}\n{}\n{}\n{}\n{}\n{}'.format(linha1,linha2,linha3,linha4,linha5,linha6))

#Função para solicitar o sabor e testar a entrada do usuário
def solicita_sabor():
    sabor = input('Digite o sabor desejado (CP/AC): ')
    sabor = sabor.upper()
    while (sabor != 'CP' and sabor != 'AC'):
        print('Sabor Inválido. Tente Novamente.')
        sabor_aux = input('Digite o sabor desejado (CP/AC): ')
        sabor = sabor_aux.upper()
    return sabor

#Função para solicitar o tamanho e testar a entrada do usuário
def solicita_tamanho():
    tamanho = input('Digite o tamanho desejado (P/M/G): ')
    tamanho = tamanho.upper()
    while (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('Tamanho Inválido. Tente Novamente.')
        tamanho_aux = input('Digite o tamanho desejado (P/M/G): ')
        tamanho = tamanho_aux.upper()
    return tamanho

#Função para definir valor do pedido de acordo com as condições de entrada de sabor e tamanho
def define_valor(sabor,tamanho):
    valor = 1
    if (sabor == 'CP' and tamanho == 'P'):
        valor = 9
        print('Você pediu cupuaçu de tamanho P: Valor R$ 9,00.')
    elif (sabor == 'CP' and tamanho == 'M'):
        valor = 14
        print('Você pediu cupuaçu de tamanho M: Valor R$ 14,00.')
    elif (sabor == 'CP' and tamanho == 'G'):
        valor = 18
        print('Você pediu cupuaçu de tamanho G: Valor R$ 18,00.')
    elif (sabor == 'AC' and tamanho == 'P'):
        valor = 11
        print('Você pediu açaí de tamanho P: Valor R$ 11,00.')
    elif (sabor == 'AC' and tamanho == 'M'):
        valor = 16
        print('Você pediu açaí de tamanho M: Valor R$ 16,00.')
    else:
        valor = 20
        print('Você pediu açaí de tamanho G: Valor R$ 20,00.')
    return valor

#Chama as funções para o primeiro pedido
sabor = solicita_sabor()
tamanho= solicita_tamanho()
valor = define_valor(sabor,tamanho)

#Pergunta se haverá outros pedidos e testa se o valor digitado foi S ou N
novo_item = input('Deseja pedir mais alguma coisa? (S/N) ')
novo_item = novo_item.upper()
if (novo_item != 'S' and novo_item != 'N'):
    while (novo_item != 'S' and novo_item != 'N'):
        print('Por favor, digite S para Sim ou N para Nao')
        novo_item = input('Deseja pedir mais alguma coisa? (S/N) ')
        novo_item = novo_item.upper()

#Soma os valores de novos pedidos
total = valor
while (novo_item == 'S'):
    sabor = solicita_sabor()
    tamanho = solicita_tamanho()
    valor = define_valor(sabor, tamanho)
    total = total + valor
    novo_item = input('Deseja pedir mais alguma coisa? (S/N) ')
    novo_item = novo_item.upper()
    if (novo_item == 'S'):
        continue
    else:
        break

#Imprime o valor total a ser pago
print('O valor total a ser pago é R$ {},00.' .format(total))

