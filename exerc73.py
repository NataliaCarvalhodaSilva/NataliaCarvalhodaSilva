# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO.
# DEPOIS MOSTRE:
#     a) APENAS OD 5 PRIMEIROS COLOCADOS;
#     b) OS ÚLTIMOS 4 COLOCADOS DA TABELA;
#     c) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA.
#     d) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.
tabela_do_campeonato_brasileiro_2021 = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceara-SC', 'Internacional', 'Sao Paulo', 'Athletico-PR', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(tabela_do_campeonato_brasileiro_2021[0:5])
print(tabela_do_campeonato_brasileiro_2021[-4:])
print(sorted(tabela_do_campeonato_brasileiro_2021))
print(tabela_do_campeonato_brasileiro_2021.index('Chapecoense')+ 1)
