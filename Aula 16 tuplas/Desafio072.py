# Escrever em uma tupla que contenha numeros de 0 a 20 por extenso
# Entrar um numero de 0 a 20 
# Retornar o numero por extenso 
linha = '=' * 20
run = True
numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while run:
    try:
        num = int(input('Digite um numero entre 0 a 20: '))
       
    except ValueError:
        print('Entre um valor valido')
    if num >= 0 and num <= 20 :
        run = False
    else:
        print('Entre um valor valido entre 0 e 20')
       

print('o numero digitado foi {}'.format(numeros[num]))    