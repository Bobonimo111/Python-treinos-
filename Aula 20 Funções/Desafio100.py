# Criar uma função que retorna uma lista
# Criar uma função que recebe uma lista e soma os numeros pares 
from time import sleep
from random import randint

fps = 0.5

def Sorteia(quant):
    """
    -> sorteia uma lista de numeros aleatorio
    :param quant: A quantidade de numeros aleatorios a serem sorteados
    :return: Uma lista
    """
    Rand_lista = list()
    print(f'Sorteando {quant} valores da lista: ',end='')
    for i in range(0,quant):
        rad = randint(0,10)
        print(f'{rad} ',end='',flush=True)
        sleep(fps)
        Rand_lista.append(rad)
    print('PRONTO!')
    return Rand_lista


def SomaPar(nuns):
    soma = 0
    for n in nuns:
        if(n%2 == 0):
            soma = soma + n
    print(f'Somando o valores pares de, {nuns}, temos {soma}.')


SomaPar(Sorteia(5))

help(Sorteia)