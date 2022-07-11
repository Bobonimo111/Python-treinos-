# Ler o nome e o preço de varios produtos
# Perguntar se quer continuar a acrescentar produtos
# Qual o total foi gasto nessa compra 
# Quantos produtos custam mais de R$ 1000
# E qual o produto mais barato





produto = ''
valor = 0 
menor = 1000000
menorNome = ''
total = 0
maisdemil = 0

linha = 25 * '- '.replace(' ','=')

while True:
    while True:
        produto = str(input('Qual o nome do produto: '))
        valor = input('Qual o valor do produto: ')
        try:
            valor = int(valor)
            break
        except ValueError:
            print('digite um valor valido')
    
    if valor < menor:
        menor = valor
        menorNome = produto

    if valor > 1000:
        maisdemil += 1
    total += valor
    if input('Deseja continua [S / N]: ').strip().lower() == 'n':
        break

print(f'Você fez um total de {total} em compras')
print(f'Sendo {menorNome} o produto mais barato custando R${menor}')
print(f'Com produtos {maisdemil} maiores de mil reais')
    