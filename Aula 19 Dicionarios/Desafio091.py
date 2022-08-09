# Cria um dicionario com quatro prosições e quatro numeros aleatorios sorteados por um dado
# Retornar o primerio segundo e terceiro lugar com base nesses dados

# Criar uma lista com o jogador e com o numero, adicionar essas listas ao dicionario, e usar o numero 
# para mudar  a posição da lista

import random
from time import sleep

PrinDic = dict()
MyListDado = list()
MyListJogador = list()
Jogador = 1
delay = 0.75 
while True:
    Radnum = random.randint(1,6) 
    if (len(MyListDado) == 0):
        MyListDado.append(Radnum)
        MyListJogador.append(Jogador)
        print(f'O jogador 1 tirou {Radnum}')
        sleep(delay)
        Jogador += 1
    elif (len(MyListDado) != 0):
        for i,v in enumerate(MyListDado):
            if (v <= Radnum):
                MyListDado.insert(i,Radnum)
                MyListJogador.insert(i,Jogador)
                print(f'O jogador {Jogador} tirou {Radnum}')
                sleep(delay)
                Jogador += 1
                break
    
    if Jogador == 5:
        break

for x in range(0,len(MyListJogador)):
    PrinDic[f'Jogador {MyListJogador[x]}'] = MyListDado[x]
print('=-'*25)
lug  = 0 

for i,v in PrinDic.items():
    lug += 1
    print(f'{lug}º o {i} com {v}')
    