#jogadores
# Entrar o nome de um jogado
# quantas partidas ele jogou 
# e quantos gols foram feitos por partida

stats = dict()
gols = list()
partidas = 0
linha = '=-'*35

stats['nome'] = str(input('Nome : '))
partidas = int(input(f'Quantas partidas {stats["nome"]} jogou: '))

for x in range(0,partidas):
    entrada = int(input(f'Quantos gols na partida {x} ? '))
    gols.append(entrada)
  
stats['gols'] = gols
stats['total'] = sum(gols)

#saída

print(linha)
print(f'{stats}.')
print(linha)

for k,v in stats.items():
    print(f'O campo {k} tem o valor {v}.')
print(linha)

print(f'O jogador {stats["nome"]} jogou um total de {partidas} partidas.')
for i,v in enumerate(gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'foi um total de {sum(gols)} gols.')