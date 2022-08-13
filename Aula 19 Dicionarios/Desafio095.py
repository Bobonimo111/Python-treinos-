# Entrar o nome, total de partidas e quantidade de gols por partida
# De quantos jogadores o usuario desejar
# Ao final retornar uma tabela, contendo o codígo, nome, os gols por partida, e o total de gols
# Dar a opção do usuario procurar por mais detalhes usando o codigo, do jogardor


CadDic = list()  #Lista principal onde tudo será adicionado
JogInf = dict()  #Dicionario onde serão adicionadas as informações do jogador
gols = list()    #lista de gols por partida na ordem

CadDic = {'nome':'joelson','partidas': 5,'golsPartida': [1,3,0,0,0]} , {'nome':'messi','partidas': 4,'golsPartida': [0,1,1,0]}

while True:
    JogInf['nome'] = str(input('Jogador nome: ').strip().lower())
    try:
        JogInf['partidas'] = int(input('Quantidade de partidas: '))
    except ValueError:
        while True:
            try:
                JogInf['partidas'] = int(input('Quantidade de partidas: '))
            except ValueError:
                print('Valor não numerico tente novamente')

    for x in range(0,JogInf['partidas']):
        gols.append(f'{x}º jogo: ')
    JogInf['golsPartida'] = gols[:]
