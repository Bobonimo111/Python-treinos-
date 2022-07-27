# Criar um tupla que contenha elementos e seus preços
# O Retorno será essa Tupla como uma listagem

MyTuple = ('Lapís',1,'Caneta',2,'Caderno',10.50,'Metro',2.50,'Panela',25,'Garrafa',12)

linha = '='*45
#Cabecalho
print(linha)
print('{:^45}'.format('LISTA DE PRODUTOS'))
print(linha) 
#Escrita da listagem
for x in range(0,len(MyTuple),2):
    print('{:.<30} R$  '.format(MyTuple[x]),end = '')
    print('{:>5}'.format(MyTuple[x+1]))    
