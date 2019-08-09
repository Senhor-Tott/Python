time = list()
jogador = dict()
partidas = list()

while True:
  jogador.clear()
  jogador['Nome'] = str(input('Nome do jogador: '))
  tot = int(input(f'Quantas partidias {jogador["Nome"]} jogou?'))
  partidas.clear()

  for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
  jogador['Gols'] = partidas[:]
  jogador['Total'] = sum(partidas)
  
  time.append(jogador.copy())

  while True:
    resp = str(input('Quer continuar?'))
    if resp in 'sn':
      break
  if resp == 'n':
    break

print('  ID ', end='')
for i in jogador.keys():
  print(f'{i:<15}',end='')

print()
for i, j in enumerate(time):
  print(f'{i:>4} ', end='')
  for d in j.values():
    print(f'{str(d):<15}', end='')
  print()

while True:
  busca = int(input('Mostrar dados ou 10 para sair: '))
  if busca == 10:
    break
  if busca >= len(time):
    print('\nErro')
  else:
    print(f'-- Dados do jogador {time[busca]["Nome"]}: ')

    for indice, gols in enumerate(time[busca]['Gols']):
      print(f'   No jogo {indice+1} fez {gols} gols')

