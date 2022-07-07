#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".


cidade = input("Entre o nome de uma cidade : ").strip()

nome_cidade = cidade.split()
linha = "="*25
if nome_cidade[0].lower() in "santos":
    print(linha)
    print("True")
    print("A cidade contem santos como primeira palavra")
    print(linha)
else:
    print(linha)
    print("False")
    print("{} não contem santos como primeira palavra".format(cidade.title()))
    print(linha)