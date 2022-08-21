#Criar uma função que realize uma contagem numerica, recebendo três paramentro inicio, fim e passo
def contador(inicio,fim,passo):
    cont = inicio
    print('\n')
    print('=-'*40)
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo} ')
    
    if(inicio < fim):
        while(True):
            if(cont > fim):
                break
            
            print(f'{cont} ',end='')
            cont = cont + passo        

    elif(inicio > fim):
        while(True):
            if(cont < fim):
                break
            
            print(f'{cont} ',end='')
            cont = cont - passo    
            



print('\n')
print('=-'*40)
print(f'Agora é sua vez de personalizar a contagem')
contador(int(input('inicio: ')),int(input('Fim: ')),int(input('Passo: ')))
