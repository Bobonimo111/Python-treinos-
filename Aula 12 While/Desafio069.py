# Um programa que cadastre pessoas com 2 variaveis idade e sexo
# onde o programa deve perguntar e não deve aceitar outra entrada além da fornecidas sendo elas F ou M ou um numero
# o programa deve finalizar ao perguntar ao usuario se ele quer finazalo  
# Ao finalizar o programa ele deve retorna total de homens +18 total de mulheres -20 e total de pessoa q
# foram cadastradas.
homens = 0
mulheres = 0 
total = 0 
sexo = ''
idade = ''
linha = ('- '*25).replace(' ','=')

stage1 = True
stage2 = True

while True:
    print(linha)
    print('CADASTRE UMA PESSOA')
    print(linha)
    while stage1:
        sexo = str(input('Masculino ou feminino [M / F]').strip())
        if sexo.lower() == 'm' or sexo.lower() == 'f':
            total += 1
            stage1 = False
        else:
            print('Valor invalido, digite um valor valido')
    while stage2:
        idade = str(input('qual a idade: ').strip())
        try:
            idade = int(idade)
            stage2 = False
        except ValueError:
            print('digite um valor valido')
    if int(idade) >= 18 and sexo.lower() == 'm':
        homens += 1
    elif int(idade) < 20 and sexo.lower() == 'f':
        mulheres += 1
    if input('deseja encerrar[S / N]: ').strip().lower() == 's':
        break   
    else: 
        stage1 = True
        stage2 = True  

print(f'Houveram ao todo {total} pessoas')
print(f'Sendo elas {homens} homens maiores de 18 ')
print(f'e {mulheres} mulheres com menos de 20 anos.')

