# Entrar quantos numeros for nescessario
# Quantos o usuario quiser
# Ñ permitir numeros repetidos
# Ao final seram retornados os valores em ordem crescente.

MyList = []

while True:
    num = int(input('Digite um numero : '))
    #logica para adicionar numero
    if (num in MyList) == False:
        MyList.append(num)
        print('Valor adicionado...')
    else:
        print('Numero repetido, ñ sera adicionado...')
    #Opção de sair do programas
    ex = str(input('Deseja sair[S / N] : ').strip())
    if ex.lower() == 's':
        break
MyList.sort()
print('=-'*25)
print(MyList)
