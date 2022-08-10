#Entrar numeros e retornalos em uma matriz

Mylist = list()
Num = list()
for line in range(0,3):
    for column in range(0,3): 
        Num.append(int(input(f'Digite um numero para a coodenada[{column},{line}]:  ')))
        if(-1 in Num):
            exit()
    Mylist.append(Num[:])
    Num.clear()

for column in range(0,3):
    for line in range(0,3):
        print(f'[ {Mylist[column][line]} ]', end='')
    print()