import datetime

# Entrada Nome, ano de nascimento, Carteira de trabalho
# Se a carteira de trabalho for diferente de 0 Requisitar ano de contratação e salario
# E dizer com quantos anos a pessoa vai se aposentar com 35 anos de contribuição

data = datetime.datetime.now()
CadDict = dict()


CadDict['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))

CadDict['idade'] = (data.year - ano)

CadDict['carteira de trabalho'] = int(input('Carteira de traballho [0 não tem]: '))

if CadDict != 0:
    CadDict['contratacao'] = int(input('Ano de contratação : '))
    CadDict['salario'] = int(input('Salario: R$ '))
    aposentadoria = CadDict['idade'] + ((CadDict['contratacao'] + 35) - data.year)

for k,v in CadDict.items():
    print(f'{k} : {v}')

if CadDict != 0 :
    print(f'Se aposenta com {aposentadoria}')