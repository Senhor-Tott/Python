from datetime import datetime
import os
import time


TURNS = 2
OPC = ''
notas = list()


# Limpar Terminal
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def inserirNotas():

	header()

	OPC = str(input('\nInforme a quantidade de avaliações\n>>> '))

	for i in range(int(OPC)):

		entrada = str(input(f'\tInforme a {i+1}º nota: ').replace(',', '.'))

		notas.append(float(entrada))

	OPC = str(input('\n[1] - Listar notas\n[*] - Sair\n>>> '))

	if OPC != '1':
		clear()
		menu()
	else:
		clear()
		header()
		listarNotas(notas)


def listarNotas(notas):

	if not notas:

		print('\n\033[1;31mNENHUM ALUNO OU NOTAS FORAM INSERIDAS!!\033[m')
		time.sleep(1)

		OPC = str(input('\n[1] - Inserir notas\n[*] - Sair\n>>> '))

		if OPC == '1':
			clear()
			inserirNotas()
		else:
			clear()
			menu()

	else:
		print('\nAvaliações\t\tNotas\t\t   Data\n')
		print('-' * 58)
		
		dataAgora = datetime.now()
		dataTexto = dataAgora.strftime('%d/%m/%Y %H:%M')

		for x in range(len(notas)):	
			print(f'{x+1}\t\t\t{notas[x]}\t\t{dataTexto}')
			print('_' * 58)

		OPC = str(input('\n[1] - Situação do Aluno\n[*] - Sair\n>>> '))

		if OPC != '1':
			clear()
			menu()
		else:
			calcularNotas(notas)


def calcularNotas(notas):

	soma = 0.0

	for x in range(len(notas)):
		soma += notas[x]

	verificarSituacao(soma)


def verificarSituacao(value):

	media = value / 2

	if media >= 7:
		print(f'\nMedia {media}\nAprovado!')

	elif media >= 3 and media < 7:
		print(f'\nMédia {media}\nRecuperação')

		OPC = str(input('\n[1] - Realizar Final\n[*] - Sair\n>>> '))

		if OPC != '1':
			clear()
			menu()
		else:

			OPC = str(input('\nInforme o valor da Final\n>>> ').replace(',', '.'))

			notas.append(float(OPC))

			verificarFinal(notas, float(OPC))

	else:
		print(f'\nMédia {media}\nReprovado!')



def verificarFinal(notas, notaFinal):

	somar = 0.0

	for x in range(len(notas)):
		somar += notas[x]

	media = (((somar / 2) * 6 )+ (notaFinal * 4)) / 10

	print(f'Média Final: {media}')

	if media >= 5:
		print('\nAprovado!')
	else:
		print('\nReprovado!')

def menu():
	print('\n')
	header()
	print('\n[1] - Inserir Notas')
	print('[2] - Listar Notas')

	OPC = str(input('\n>>> '))

	if OPC == '1':
		clear()
		inserirNotas()
	elif OPC == '2':
		clear()
		listarNotas(notas)


def header():
	print('\n')
	print('=' * 58)
	print('=' * 19, ' Sistema de Notas ', '=' * 19)
	print('=' * 58)

menu()