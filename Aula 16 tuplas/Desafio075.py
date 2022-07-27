#Entrar 4 numeros pelo teclado 
#Saida
# Quantas vezes o valor 9 foi digitado
# Em qual posição o valor 3 foi digitado
# E quantos numeros pares foram digitado 

pares = 0
nove = 0
MyList = []

for x in range(4):
    MyList.append(int(input('Digite um numero: ')))

MyTuple = tuple(MyList)

for t in MyTuple:
    if t%2 == 0 and t != 0 :
        pares += 1 

for t in MyTuple:
    if t == 9:
        nove += 1

print('=-'*50)
try:
    if MyTuple.index(3) != -1:
        print(f'O valor 3 foi econtrado na posição {MyTuple.index(3)+1}')
except ValueError:
    print(f'O valor 3 não foi digitado')


print(f'O valor 9 foi digitado {nove} vezes')
print(f'O total de numeros pares foi de {pares}')