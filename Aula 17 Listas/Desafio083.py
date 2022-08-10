# Entrar uma expressão usando parenteses
# Saida dizer se os parenteses foram usados de forma correta ou não 

entrada = input('Digite uma expressão: ').strip()
MyList = []
#Vai quebrar toda a string em uma Lista
for x in entrada:
    MyList.append(x)

#Chegar se a quantidade de parenteses é par ou não
if ((MyList.count('(') + MyList.count(')')) % 2 == 0 ):
    print('A expressão usou corretamente os parenteses')
else:
    print('A expressão é invalida')
