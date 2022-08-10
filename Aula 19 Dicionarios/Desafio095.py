# Entrar o nome, total de partidas e quantidade de gols por partida
# De quantos jogadores o usuario desejar
# Ao final retornar uma tabela, contendo o codígo, nome, os gols por partida, e o total de gols
# Dar a opção do usuario procurar por mais detalhes usando o codigo, do jogardor


CadDic = {'nome':'joelson','partidas': 5,'golsPartida': [1,3,0,0,0]} , {'nome':'messi','partidas': 4,'golsPartida': [0,1,1,0]}
JogInf = dict()

while True:
    JogInf['nome'] = str(input('Jogador nome: ').strip().lower())
    JogInf['partidas'] = int(input('Quantidade de partidas: '))


    JogInf['golsPartida']