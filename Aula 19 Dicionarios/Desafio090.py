# Entra o nome de um aluno e a media 
# Retornar o nome a media e a situação [Aprovado ou reprovado]

MyDic = {}

MyDic['Nome'] = str(input('Qual o nome do aluno: '))
MyDic['Média'] = int(input('Qual a média: '))

#check se está aprovado ou reprovado

if (MyDic['Média'] >= 6):
    MyDic['Situação'] = 'Aprovado'
else:
    MyDic['Situação'] = 'Reprovado'

for k,v in MyDic.items():
    print(f'O {k} é igual a {v}')