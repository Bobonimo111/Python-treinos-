#Criar um função que receba um texto qualquer de entrada 
#E que printe na tela esse testo com linha do mesmo tamanho 
def escreva(text):
    text_size = len(text)
    print('~'*(text_size+4))
    print(text.center(text_size+4))
    print('~'*(text_size+4))



escreva('William')
escreva('Curso em video')
escreva('Ola mundo')