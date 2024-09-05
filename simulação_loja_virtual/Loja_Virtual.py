#Boas Vindas
print('Prezado cliente, seja bem vindo a loja do Nelson Emeliano Silva - RU: 4666213')

#Solicita para o usuário o valor unitário e a quantidade do produto
vunitario = float(input('Digite o valor unitário do produto que deseja comprar: '))
qtd = int(input('Digite a quantidade do produto: '))

#Calcula o valor total do pedido
vtotal = vunitario * qtd
desconto = {}

#Identifica qual a porcentagem de desconto sobre o produto de acordo com o valor total do pedido.
if (vtotal < 2500):
    desconto = 0
elif (vtotal >= 2500 and vtotal < 6000):
    desconto = 0.04
elif (vtotal >= 6000 and vtotal < 10000):
    desconto = 0.07
else:
    desconto = 0.11

#Calcula o valor final do produto com desconto.
vdesconto = vtotal - (vtotal * desconto)

#Imprime na tela o valor total do pedido.
print('O valor de sua compra sem desconto foi de R${:.2f}.'.format(vtotal))

#imprime na tela uma mensagem para o usuário de acordo com o valor de desconto.
if (vtotal < 2500):
    print('O valor de sua compra com desconto foi de R${:.2f} (desconto de 0%),'.format(vdesconto),'obtenha desconto em compras no valor de R$2500.00 ou mais.')
elif (vtotal >= 2500 and vtotal < 6000):
    print('O valor de sua compra com desconto foi de R${:.2f} (desconto de 4%).'.format(vdesconto))
elif (vtotal >= 2500 and vtotal < 10000):
    print('O valor de sua compra com desconto foi de R${:.2f} (desconto de 7%).'.format(vdesconto))
else:
    print('O valor de sua compra com desconto foi de R${:.2f} (desconto de 11%).'.format(vdesconto))