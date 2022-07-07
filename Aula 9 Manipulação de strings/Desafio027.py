#   027: Faça um programa que leia o 
#   nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Entre seu nome completo : ').strip()
nome_quebrado = nome.split()
linha = '=' *75

#armazena a primeira e ultima string da list, ou seja primeiro e ultimo nome 
nome1 = nome_quebrado[0]
nome2 = nome_quebrado[len(nome_quebrado)-1]

print('\n'+linha +'\n')
print('ola {} \n seu primeiro nome é {} \n e o ultimo é {}'.format(nome,nome1,nome2))