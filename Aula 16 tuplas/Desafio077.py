# Criar uma tupla com varias palavras
# E retornar cada palavra e quais suas vogais

MyTuple = ('milho','pilha','amor','cintia','toxico','espaço','pamonha','gato','verbo','ansiedade')

for palavra in MyTuple:
    vogal = ''
    for letra in palavra:
        if letra.lower() == 'a':
            vogal += 'a '
        elif letra.lower() == 'e':
            vogal += 'e '
        elif letra.lower() == 'i':
            vogal += 'i '
        elif letra.lower() == 'o':
            vogal += 'o '
        elif letra.lower() == 'u':
            vogal += 'u '
    print('{:<40} {}'.format(f'A palvra {palavra.upper()} possui as vogais',vogal))