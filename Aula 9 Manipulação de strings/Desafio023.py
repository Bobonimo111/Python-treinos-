#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num1 = input("entre um numero")
nome = ""
#Separar letra por letra 
for a in num1:
    print(a)
    nome += '{} '.format(a)

print(nome)