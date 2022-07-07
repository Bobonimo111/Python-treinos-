#   Testes para ver os if's aninhados e o for

altura = [120,125,160,190]
peso = [50,54,55,64]
entrada = int(input("Qual sua altura em cm : "))
cont = False
for i in altura:
        
    if i == entrada:
        loc = altura.index(i)
        print("seu peso é aproximadamente {}".format(peso[loc]))
        cont = True
        break
if  cont == False:
    print("Sua altura não consta no banco de dados")
