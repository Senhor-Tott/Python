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
