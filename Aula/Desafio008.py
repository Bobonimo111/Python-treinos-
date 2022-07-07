#entrar metros e exibir em centrimetros e milimetros
Entrada = input('Entre os metros: ')
metros = int(Entrada)

centimentros = metros * 100
milimetros = metros * 1000

print('{} metros possui {} centímetros e {} milímetros'.format(metros,centimentros,milimetros))