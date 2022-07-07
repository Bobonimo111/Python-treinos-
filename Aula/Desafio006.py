#dobro, triplo e sqrt 

entrada = input('Entre um numero: ')
is_num = True
while is_num:
    if (entrada.isnumeric()):
        numero = int(entrada)
        is_num = False
    else:
        entrada = input('Valor invalido, entre um valor valido: ')


dobro = numero * 2
triplo = numero * 3 
raiz = numero ** (1/2)

print('Entrada {} \ndobro {} \ntriplo {} \nraiz {:.5f}'.format(numero,dobro,triplo,raiz))