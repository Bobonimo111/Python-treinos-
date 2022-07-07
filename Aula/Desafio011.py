# calcular a área quadrada de uma parede, e calcular quantos litros de tinta seria nescessario 
# para pinta-la, sendo que 1L pintam 2m quadrados
#F(x) = x/2 or tinta = area / 2



altura = int(input('Qual a altura da parede: '))
largura = int(input('Qual a largura a da parede: '))
area = altura * largura
tinta = area/2
print('São necessários {} litros para pintar {}m²'.format(tinta,area))


