# Cria um dicionario com quatro prosições e quatro numeros aleatorios sorteados por um dado
# Retornar o primerio segundo e terceiro lugar com base nesses dados

# Criar uma lista com o jogador e com o numero, adicionar essas listas ao dicionario, e usar o numero 
# para mudar  a posição da lista

from random import randint
from time import sleep
MyDict = dict()
lugar = 1
delay = 0.75

print('{:^50}'.format('JOGO DOS DADOS'))

print("-="*30)
#Organiza o dicionario, e retorna suas Keys, onde elas são usadas pra chamar
for x in range(1,5):
    MyDict[f'jogador {x}'] = randint(1,6)
    print(f'{"jogador {}".format(x)} tirou no {MyDict["jogador {}".format(x)]} dado')
    sleep(delay)

print("-="*30)

for keys in sorted(MyDict , key= MyDict.get, reverse=True):
    print(f'{lugar}º {keys} com {MyDict[keys]}')
    sleep(delay)