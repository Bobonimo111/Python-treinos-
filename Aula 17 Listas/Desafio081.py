# Entrar varios numeros numa lista
# Saída :
# Quantos numeros foram digitado
# Os numeros em ordem decrescente
# Se o valor 5 está ou não la lista
 
MyList = []
while True:
    MyList.append(int(input('Digite um numero: ')))
    if str(input('Deseja continuar[S/N]: ')).strip().lower() == 'n':
        break

print(f'Foram digitados {len(MyList)+1}')
print(f'Sendo os valores em ordem decrescente {sorted(MyList,reverse=True)}')
if 5 in MyList:
    print('O valor 5 se encontra listado...')
else:
    print('O valor 5 não se encontra listado...')