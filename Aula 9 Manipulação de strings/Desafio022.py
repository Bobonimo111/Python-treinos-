#   Crie um programa que leia o nome completo de uma pessoa e mostre: - 
# O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome =  input("Qual o seu nome completo: ").strip()
#possui 13 letras(sem espaços)

print(nome.upper())
print(nome.lower())

#separa as palavras para poder contalas
cont = 0 
for a in nome.split():
    #cont vai receber ele mais o tamanho da palavra a ser contada
    cont += len(a.strip())

print("O nome {} possui {} letras".format(nome,cont))