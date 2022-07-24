#Entrar cinco numeros
#Saida 
#Qual foi o menor e o maior valor e em quais posições eles estão, se for mais de um 

numeros = []
for x in range(0,5):
    numeros.append(input('Digite um numero : '))

numeorosOrdenados = sorted(numeros)

linha = '=-'*30
print(linha)
print(f'Os numeros digitados foram {numeros}')

print(f'O menor numero foi {numeorosOrdenados[0]}, nas posições : ', end = '')
for I,V in enumerate(numeros):
    if (numeorosOrdenados[0] == V):
        print(f'{I}... ',end='')
print(f'\nO maior numero foi {numeorosOrdenados[-1]}, nas posições : ', end='')
for I,V in enumerate(numeros):
    if (numeorosOrdenados[-1] == V):
        print(f'{I}... ',end = '')

print(f'\n{linha}')
      