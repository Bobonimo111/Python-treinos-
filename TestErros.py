from ast import Break


num = 0

try:
    num = int(input('Quantidade de partidas: '))
except ValueError:
    while True:
        try:
            print('Valor não numerico tente novamente')
            num = int(input('Quantidade de partidas: '))
        except:
            print('',end='')
        else:
            break