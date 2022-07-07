#entrar com um angulo e retornar o seu a valor de seno e cosseno e tangend
from math import sin, cos,tan,degrees,radians

#entrada primaria e inicialização de variaveis
ang = int(input("qual o angulo? :"))
seno = 0
cosseno = 0
tangent = 0 

#convertendo a entrada para radianos, para realização de calculos
rad = radians(ang)

seno = sin(rad)

cosseno = cos(rad)

tangente = tan(rad)

#Saida com os resultados corretos
print("seu angulo {0} \n O seno {1:.3f} \n O cosseno {2:.3f} \n A tangente {3:.3f} ".format(ang,seno,cosseno,tangente))

