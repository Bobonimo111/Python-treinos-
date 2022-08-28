#Criar uma função chamada maior
#E com base nela ler varios numeros e dizer qual foi o maior numero com pausa de timer

from time import sleep
fps = 0.4


#Função que vai escrever o maior numero, na tela
def Maior(*num):
    
    print('=-'*30)

    print('Analizando valores passados...')
    maior = 0   
    for n in num:
        print(f'{n} ',end='',flush=True)
        sleep(fps)
        if(n > maior):
            maior = n
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    
    print('=-'*30)

Maior(1,2,3,6,5,4)
Maior()

