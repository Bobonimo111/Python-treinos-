#Ler o salario de um funcionario e dar um acrescimo de 15%

salario = int(input('Quanto é o seu salario em R$: '))
acrescimo = (salario*(15/100))

print('o salario foi de R$ {0:.2f} para R$ {2:.2f} com {1:.2f} de acrescimo, sendo de 15%'.format(salario,acrescimo,(salario+acrescimo)))