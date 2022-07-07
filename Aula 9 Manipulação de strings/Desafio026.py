#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input("Entre uma frase: ")

a_quantidades = (frase.lower()).count("a")
a1 = None
a2 = None
#Vai localizar o primeiro A
if (frase.lower()).find('a') != -1 :
    a1  = (frase.lower()).find('a')

for a in range(len(frase)):
    if (frase.lower()).find('a',a) != -1 :
        a2 = a
        
        
   
print("A frase possui {} a's e também possui a's nas possições \n inicial : {} \n final : {} ".format(a_quantidades,a1,a2))
