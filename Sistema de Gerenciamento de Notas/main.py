try:
    # Imports de bibliotecas
    import os
    import time
    from datetime import date
    from datetime import datetime

    TURNS = 2
    CALC = 2

    notas = list()
    n = list()
    soma = 0.0
    notaFinal = 0.0
    media = 0.0

    validation = False
    expired = False

    def Clear():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")


    #Calculando o Resultado Final
    def calcFinal(m, nota):

        global validation, expired

        mediaFinal = (m * 6 + nota * 4) / 10

        if mediaFinal >= 5:
            validation = True
            expired = True
        else:
            validation = False
            expired = True


    #Varificando Situação do Aluno
    def situacaoAluno():
        
        global soma, media, notaFinal

        if soma == 0:
            for i in range(TURNS):
                soma += notas[i]

        media = soma / CALC

        print(f'\nMedia: {media}')

        if validation or expired:
            mediaFinal = (media * 6 + notaFinal * 4) / 10
            print(f'\nMedia Final: {mediaFinal}')

            if mediaFinal >= 5:
                print('\n\033[1;32mAPROVADO na prova Final!\033[m')
            else:
                print('\n\033[1;31mREPROVADO na prova Final\033[m')

            opc = str(input('\n[*] - Sair\n>>> '))

            if opc != '1' or opc == '1':
                Clear()
                menu()
        else:

            if media >= 7:
                print('\n\033[1;32mAPROVADO!\033[m')

            elif 7 > media >= 3:
                print('\n\033[1;33mRECUPERAÇÃO!\033[m')

                opc = str(input('\n[1] - Realizar prova Final\n[*] - Sair\n>>> '))

                if opc != '1':
                    Clear()
                    menu()

                notaFinal = float(input('\nNota Final:  '))
                calcFinal(media, notaFinal)

            elif media < 3:
                print('\n\033[1;32mREPROVADO!\033[m')

            Clear()
            header()
            situacaoAluno()


    #Exibindos as notas
    def listarNotas():

        global notaFinal
        try:
            Clear()
            header()

            print('\n\nAvaliação\t   Nota\t\t         Data')
            print('-'*52)

            for x in range(0, TURNS):

                data_hora = datetime.now()
                data_atual = data_hora.strftime('%d/%m/%Y %H:%M')
        
                print(f"    {x+1}º\t\t   {notas[x]}\t\t   {data_atual}")
                print('_'*52)

            print('\n[1] - Verificar Situação do aluno\n[*] - Sair')
            
            opc = str(input('\n>>> '))

            if opc != '1':
                Clear()
                menu()
            
            situacaoAluno()
            
        except (ValueError, TypeError, IndexError):
            print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
            time.sleep(1)
            Clear()
            menu()


    #Adicionando Notas no Vetor
    def inserirNotas():
        try:
            global validation, expired
            global soma, media, notaFinal

            header()
            if not notas:
                for x in range(TURNS):

                    entrada = str(input(f'\nInforme a {x+1}º nota\n>>> ')).replace(',', '.')

                    if float(entrada) > 10:
                        print('\n\033[1;32mValor maior que o permitido!\033[m')
                        time.sleep(1)
                        entrada = ''
                        notas.clear()
                        inserirNotas()

                    elif float(entrada) < 0:
                        print('\n\033[1;32mValor menor que o permitido!\033[m')
                        time.sleep(1)
                        entrada = ''
                        notas.clear()
                        inserirNotas()

                    notas.append(float(entrada))

                if notas:
                    n.append(notas[:])
                    print('\n\033[1;32mNotas inseridas com sucesso!\033[m')
                    time.sleep(1)
                    Clear()
                    menu()

            else:
                print('\nDeseja inserir novas notas?')
                op = str(input('\n[1] - Continuar\n[*] - Sair'))

                if op != '1':
                    Clear()
                    menu()
                else:
                    notas.clear()
                    validation = False
                    expired = False
                    media = 0
                    soma = 0
                    notaFinal = 0
                    Clear()
                    inserirNotas()

        except (ValueError, TypeError):
            print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
            time.sleep(1)
            Clear()
            menu()


    #Função de seleção de Menu
    def Opc(opc):
        if opc == '1':
            Clear()
            inserirNotas()
        elif opc == '2':
            Clear()
            listarNotas()
        else:
            menu()


    # Cabeçalho e Menu
    def menu():
        header()
        print("\n[1] - Inserir Notas")
        print("[2] - Listar Notas")
        print("[*] - Sair")

        opc = str(input("\n>>> "))

        Opc(opc)

    def header():
        print("\n")
        print("==" * 26)
        print("==" * 8, " Sistema de Notas ", "==" * 8)

    Clear()
    menu()

except KeyboardInterrupt:
    print('\n\033[1;32mVolte Sempre\033[m')
