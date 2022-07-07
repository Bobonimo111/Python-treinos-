#Ler um numero real e mostra apenas sua parte inteira
import math


numero = float(input("Digite um numero real: "))


print("O numero sem casas decimais é {}".format((math.trunc(numero))))