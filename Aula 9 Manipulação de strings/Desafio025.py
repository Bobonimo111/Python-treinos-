# Entrar o nome de uma pessoa e dizer se ela possui ou não Silva no nome

nome = input("Qual seu nome completo : ").strip()
nome_l = nome.split()


if "silva" in nome.lower():
    print("contem silva no nome : {}".format(nome.title()))

        