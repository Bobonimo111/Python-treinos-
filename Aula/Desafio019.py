#Sortear um aluno dentre quatro.
import random

alunos = ["Jóse algusto","Carlos Daniel","Jainara dos santos","Oliver"]

numero_aleatorio = random.randrange(4)

print(numero_aleatorio)
print("O sorteado foi: {}".format(alunos[numero_aleatorio]))