#Entrar um numero e exibir sua tabuada 

numero = int(input('Entre um numero para exibir-mos sua tabuada: '))
for x in range(10+1):
    print('{:^5}X{:^5}={:^5}'.format(numero,x,(x*numero)))