from time import sleep

# Entrar o nome,sexo[M , F] e a idade
# Retornar o total de pessoas -
# A media de idade
# O nome das mulheres cadastradas
# A lista das pessoas que estão acima da média 


tempo = 0.75
IndDic = dict()
CadList = list()

#Area de cadastros
while True:

    IndDic['nome'] = str(input('Nome: ')).strip().lower()
    IndDic['sexo'] = str(input('Sexo [M/F]: ')).strip().lower()
    IndDic['idade'] = int(input('Idade: '))
    
    CadList.append(IndDic.copy())
    IndDic.clear()
    
    if input('Quer continuar[S / N]:  ' ).strip().lower() == 'n':
        break
    
#Area logica 

#Faz a soma de todas as idades
soma = 0
for x in CadList:
    soma += x['idade']

#Guarda as mulhers em outra lista especifica
mulheres = list()
for x in CadList:
    if (x['sexo'] == 'f'):
        mulheres.append(x['nome']) 


AcimaDaMedia = list()
for x in CadList:
    if (soma/len(CadList) < x['idade']):
        AcimaDaMedia.append(x.copy())       


#Area de retorno
print('=-'*35)
print(f'- O grupo tem {len(CadList)} pessoas.')
print(f'- A media de idade é de {soma/len(CadList)}.')
print(f'- Mulheres cadastradas foram {", ".join(mulheres)}.')
print(f'- O total de pessoas acima da media {len(AcimaDaMedia)}, segue a lista: \n')
sleep(tempo)
for x in AcimaDaMedia:
    print(f'    {x}')
    sleep(tempo)
print('\n  << Encerrado >>')