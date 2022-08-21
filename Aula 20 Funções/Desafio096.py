#Fazer uma função que recebe a base e a largura
#Retorne a área 
def area(largura,comprimento):
    
    print(f'A aréa de um terreno de {largura:.1f} X {comprimento:.1f} é de {comprimento*largura:.1f}')


largura = input('Largura (m): ')
comprimento = input('comprimento (m): ')
area(float(largura),float(comprimento))