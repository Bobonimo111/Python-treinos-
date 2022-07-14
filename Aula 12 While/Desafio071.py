#entrada um valor de dinheiro a ser sacado
#saida a quantida de notas de 50,20,10 e 1 real que serão sacadas.

dinheiro = 0 
d50 = 0
d20 = 0 
d10 = 0 
d01 = 0 
linha = 25*'- '.replace(' ','=')

while True:
    while True:
        try:
            dinheiro = int(input('Quanto deseja sacar R$: '))
            break
        except ValueError:
            print('digite um valor valido')

    if dinheiro >= 50:
        d50 = int(dinheiro // 50)
        d20 = int((dinheiro % 50) // 20 )
        d10 = int(((dinheiro % 50) % 20) // 10 )
        d01 = int(((dinheiro % 50 ) % 20 ) % 10 )
    elif dinheiro < 50 and dinheiro > 20:
        d20 = int(dinheiro // 20)
        d10 = int((dinheiro % 20) // 10)
        d01 = int((dinheiro % 20) % 10) 
    elif dinheiro <= 20 and dinheiro >= 10:
        d10 = int(dinheiro // 10) 
        d01 = int((dinheiro % 10))
    else:
        d01 = int(dinheiro)
     
    print('{linha} \n -----Notas----- \n R$50,00: {d50:<2} \n R$20,00: {d20:<2} \n R$10,00: {d10:<2} \n R$1,00:  {d01:<2} \n {linha}')
    
    break