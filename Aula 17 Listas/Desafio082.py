# Entrar quantos numeros o usuario quiser 
# Saída
# Uma lista com os numeros Pares 
# Uma lista com os numeros Impares

MyList = []
NumPares = []
NumImpars = []

#Entradas

while True:
    MyList.append(int(input('Digite um valor: ').strip()))
    if str(input('Deseja continuar [S/N]: ')).strip().lower() == 'n':
        break

#loop para checar e adicionar cada item em suas determinadas listas

for x in MyList:
    if (x % 2 == 0):
        NumPares.append(x)
    else:
        NumImpars.append(x)

#Saidas

print(f'Os numeros digitados foram {MyList}')
print(f'OS numeros pares foram {NumPares}')
print(f'Os numeros impares foram {NumImpars}')