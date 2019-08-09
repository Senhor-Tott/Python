"""print('\033[1;31mVermelho\033[m')
print('\033[1;32mVerde\033[m')
print('\033[1;33mAmarelo\033[m')
print('\033[1;34mAzul\033[m')"""
from insertNotes import *


#Menu 
def Menu():
    Header()
    print('\n[1] - Inserir Notas')
    print('[2] - Listar Notas')
    print('[3] - Visualizar Situação')
    print('[*] - Sair')

    opc = input('>>> ')

    if(opc == '1'):
        InsertNotes()
    elif(opc == '2'):
        print('')
    elif(opc == '3'):
        print('')
    else:
        print('')

def Header():
    print('\n')
    print('-=' * 20)
    print('-=' * 4, 'Gerenciamente de Notas', '-=' * 4)

Menu()
