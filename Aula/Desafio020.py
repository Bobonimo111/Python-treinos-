#Retornar uma sequencia de alunos, para apresentar um semeninario

import random

alunos = ["Jóse algusto","Carlos Daniel","Jainara dos santos","Oliver"]

print(random.sample(alunos, k=4))
random.shuffle(alunos)
print(alunos)