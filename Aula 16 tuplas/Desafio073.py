# Em uma tupla colocar os 20 primeiros colocados do campeonato brasileiro de futebol
# Retorna
# A) os cinco primeiros colocados
# B) Os 4 ultimo colocados 
# C) Uma lista em ordem alfabetica
# D) Em que posição está a chapecoence


Cbraisileiro = ('Palmeiras','Corinthians','Internacional','Atlético Mineiro','Fluminense','Athletico-PR','São Paulo','Santos','Flamengo','Botafogo','Bragantino','Goiás','Cuiabá','Coritiba','América-MG','Avaí','Ceará','Atrético Goianiense','juventude','Fortaleza')
linha =50*'=-'

# Os cinco primeiros times
print(' {0} \n {2:>55} \n {1} '.format(linha,Cbraisileiro[:5],'OS cinco primeiros times são'))

# Os quatro ultimos
print(linha)
print('{:>53}'.format('Os quatro ultimos times'))
print(Cbraisileiro[-5:])


# A lista em ordem alfabetica 
print(linha)
print('{:>53}'.format('A lista em ordem alfabetica'))
print(sorted(Cbraisileiro))

#Em que posição está a chapecoence... como não tem chapecoence vou no Flamengo
print(linha)
print('A posição do flamengo na lista é a {}ª \n'.format(Cbraisileiro.index('Flamengo')+1))

