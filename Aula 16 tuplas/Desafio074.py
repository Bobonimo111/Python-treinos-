import random

#Gerar cinco numeros aleatorio e armazenar numa tupla
#Saida 
#Mostrar quais foram os valors
#Qual foi o menor e o maior valor 



Lista = []
MyTuple = ()

for x in range(5):
    Lista.append(random.randint(0,50))

MyTuple = tuple(sorted(Lista)) 

print(f'Os numeros sorteados foram {MyTuple}')
print(f'O maior numero {MyTuple[-1]} e o menor {MyTuple[0]}')