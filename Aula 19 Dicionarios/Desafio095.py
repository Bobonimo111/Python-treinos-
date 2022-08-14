# Entrar o nome, total de partidas e quantidade de gols por partida
# De quantos jogadores o usuario desejar
# Ao final retornar uma tabela, contendo o codígo, nome, os gols por partida, e o total de gols
# Dar a opção do usuario procurar por mais detalhes usando o codigo, do jogardor


BdJogadores = list()  #Lista principal onde tudo será adicionado
JogInf = dict()  #Dicionario onde serão adicionadas as informações do jogador
gols = list()    #lista de gols por partida na ordem

BdJogadores = [{'nome':'joelson','partidas': 5,'golsPartida': [1,3,0,0,0]} , {'nome':'messi','partidas': 4,'golsPartida': [0,1,1,0]}]

while True:
    JogInf['nome'] = str(input('Jogador nome: ').strip().lower())
    try:
        JogInf['partidas'] = int(input('Quantidade de partidas: '))
    except ValueError:
        while True:
            try:
                print('Valor não numerico tente novamente')
                JogInf['partidas'] = int(input('Quantidade de partidas: '))
            except ValueError:
                print('')
            else:
                break

    for x in range(0,JogInf['partidas']):
        gols.append(int(input(f'gols no jogo {x}º : ')))
    
    JogInf['golsPartida'] = gols[:]     #Adiciona a lista de gols ao dicionario 
    BdJogadores.append(JogInf.copy())   #Copia o dicionario para a lista como banco de dados

    #Limpa os campos para não ocorrer nenhum imprevisto
    gols.clear() 
    JogInf.clear()

    if input('Deseja continuar[S/N]: ').strip().lower() == 'n':
        break


print('=-'*40)
print('{:<5}{:<15}{:<15}{:<20}{:<3}'.format('ID' , 'NOME' , 'PARTIDAS' , 'GOLS' , 'TOTAL'))
print('-'*80)
for i in range(0,len(BdJogadores)): #for para fazer uma tabela 
    golsT = sum(BdJogadores[i]['golsPartida'])
    print('{:<5}{:<15}{:<15}{:<20}'.format(i,BdJogadores[i]['nome'],BdJogadores[i]['partidas'],str(BdJogadores[i]['golsPartida'])),end='')
    # Nesse print acima, taco os testos tudo a direta com o espaçamento definidocls
    
    print(golsT)
print('-'*80)
while True:
    CodJogador = int(input('Mostrar dados de qual jogador: ')) # Variavel q leva o codigo do jogador
    if (CodJogador <= (len(BdJogadores) - 1) and CodJogador >= 0) : # Teste Pra ver se o id esta presente no comprimento da lista
        print(f'-- LEVANTAMENTO DO JOGADOR {BdJogadores[CodJogador]["nome"]}') 
        for i,v in enumerate(BdJogadores[CodJogador]['golsPartida']): #for pra imprimir os gols por partid 
            print(f'No {i}º jogo fez {v} gols.')
    elif(CodJogador == -1): # Se digitar -1 o programa se encerra
        print('==>> Progama encerrado <<==')
        break
    else:  # Se não estiver no range definido o programa pedira um novo numero 
        print(f'O codigo {CodJogador} não esta presente!!')