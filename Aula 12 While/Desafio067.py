#Ler um nomero qualquer e retornar sua taboada de 0 a 10 ou ate 20 lado a lado 

# Barinhas de separação 
import time
barinha = '-'*50

print('\n         Gerador de taboadas')
while True:
    num = int(input('Qual taboada deseja saber ? '))
    #termina o loop se a entrada do programa for menor de que zero
    if num < 0:
        print('encerrando...')
        break
    
    print(barinha)
    #realiza o e imprime os calculos da taboada
    for i in range(0,10+1):
        print('{} * {} = {}'.format(num,i,i*num))
    print(barinha)
