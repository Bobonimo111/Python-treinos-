#Entrar um preço e dar um desconto de 5% nele

preco = int(input('Entre o preço: '))
descontado = preco - (preco *(5/100))
print('O valor do item foi de R${:.2f} para R${:.2f}'.format(preco,descontado))