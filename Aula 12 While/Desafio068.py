#Par ou impar, o jogador deve entrar um numero depois escolhe um numero.


import random


pi = ''
num1 = 0 
numPc = 0
vitoria = True 
vitoriaCont = 0 
linha = ('= '*25).replace(' ','-')

print('Par ou impar!!')
while True:
    print(linha)
    num1 = int(input('Qual numero você deseja? '))
    print(linha)
    pi =  str(input('Par ou impar[P / I] ')).strip()
    print(linha)
    numPc = random.randrange(0,10)
    
    #Checa se o par ganhou ou perdeu

    if (num1+numPc)%2 == 0 and pi.lower() == 'p':

        print(f'Você ganhou o {num1} + Pc = {numPc} são pares')
   
        vitoriaCont += 1

    elif (num1+numPc)%2 == 0 and pi.lower() != 'p':
        print(f'Você perdeu o {num1} + PC = {numPc} são impares')
        print(f'Você obteve um total de {vitoriaCont} vitorias consecutivas')
        break
    elif (num1+numPc)%2 != 0 and pi.lower() == 'i':

        print(f'Você ganhou {num1} + Pc = {numPc} são impares') 

        vitoriaCont += 1 

    else:
        print(f'você perdeu {num1} + Pc ={numPc} são impares.')
        print(f'Você obteve um total de {vitoriaCont} vitorias consecutivas')
        break