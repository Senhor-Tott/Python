turma = list()
alunos = dict()
notas = list()

while True:
  alunos.clear()
  alunos['Nome'] = str(input('Nome do Aluno: '))
  tot = int(input(f'Quantas avaliações feitas pelo {alunos["Nome"]}?\n>>> '))
  notas.clear()

  for c in range(0, tot):
    notas.append(int(input(f'     Valor da {c+1}º nota: ')))
  alunos['Notas'] = notas[:]
  alunos['Media'] = sum(notas)
  
  turma.append(alunos.copy())

  print()

  while True:
    resp = str(input('Quer continuar?'))
    if resp in 'sn':
      break
  if resp == 'n':
    break

print('ID ', end='')
for i in alunos.keys():
  print(f'{i:^28}',end='')

print()

for indice, j in enumerate(turma):
  print(f'{indice:^4} ', end='')
  for dado in j.values():
    print(f'{str(dado):^27}', end='')
  print()
  print('_'*80)

print()

while True:
  busca = int(input('Mostrar dados ou 10 para sair: '))
  if busca == 10:
    break
  if busca >= len(turma):
    print('\nErro')
  else:
    print(f'-- Dados do Aluno {turma[busca]["Nome"]}: ')

    for indice, notas in enumerate(turma[busca]['Notas']):
      print(f'     An avalição {indice+1} fez {notas} pontos')

