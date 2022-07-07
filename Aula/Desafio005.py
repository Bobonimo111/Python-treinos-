#Sucessor e antecessor
entrada = input('entre um numero: ')
nom_numeric = True
while nom_numeric:
    if (entrada.isnumeric()):
        numero = int(entrada)
        nom_numeric = False
    else:
        entrada = input('{} não é um valor valido \nEntre um valor valido: '.format(entrada))

print(' Antecessor: {0} \n > \n Entrada: {1} \n > \n Sucessor: {2} '.format(numero - 1,numero,numero + 1))