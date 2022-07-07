#Receber o CO e CA de um triangulo retangulo e calcular sua hipotenusa
# a²= b² + c²
from math import pow, sqrt, trunc

ca = int(input('qual cateto adjacente: '))
co = int(input('qual cateto oposto: '))

hip = sqrt(pow(ca,2) + pow(co,2))

print('A hipotenusa é igual a: {}'.format(trunc(hip)))