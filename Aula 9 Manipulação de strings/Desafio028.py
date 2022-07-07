#028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário descobrir qual foi 
# o número escolhido pelo computador. -O programa deverá escrever na tela se o usúario venceu ou perdeu.
import random

numero_R = random.randrange(1,6)

print(numero_R)
entrada = int(input("qual o numero secreto de 1 a 5 ").strip())


print('você acertou' if numero_R == entrada else 'você errou, o numero é {0}'.format(numero_R))