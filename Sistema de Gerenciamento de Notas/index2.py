try:
    from datetime import datetime
    import os
    import time

    CALC = 3
    OPC = ''
    notas = list()
    validation = False
    expiration = False


    # Limpar Terminal
    def clear():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

    #Inserindo Notas
    def inserirNotas():

        try:
            if not notas:
                header()

                OPC = str(input('\nInforme a quantidade de avaliações realizadas\n>>> '))

                for i in range(int(OPC)):

                    try:
                        entrada = str(input(f'\tInforme a {i + 1}º nota: ').replace(',', '.'))

                        if (float(entrada) >= 0) and (float(entrada) <= 10):
                            notas.append(float(entrada))

                        else:
                            if float(entrada) < 0:
                                print('\n\033[1;31mNota menor que zero!\033[m')
                            elif float(entrada) > 10:
                                print('\n\033[1;31mNota maior que o permitido!\033[m')
                            notas.clear()

                            OPC = str(input('\n[1] - Inserir notas\n[*] - Sair\n>>> '))

                            if OPC != '1':
                                clear()
                                menu()
                            else:
                                clear()
                                inserirNotas()
                    except (ValueError, TypeError):
                        print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
                        print(f'\033[1;31m{entrada.upper()} não é um valor numérico!\033[m')
                        time.sleep(2)
                        notas.clear()
                        clear()
                        inserirNotas()

                OPC = str(input('\n[1] - Listar notas\n[*] - Sair\n>>> '))

                if OPC != '1':
                    clear()
                    menu()
                else:
                    clear()
                    header()
                    listarNotas(notas)
            else:
                OPC = str(input('\n[1] - Inserir novas notas\n[*] - Sair\n>>> '))

                if OPC != '1':
                    clear()
                    menu()
                else:
                    notas.clear()
                    clear()
                    inserirNotas()
        except (ValueError, TypeError):
            print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
            time.sleep(1)
            clear()
            menu()


    #Listando Notas
    def listarNotas(notas):
        if not notas:

            header()
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
                print(f'{x + 1}\t\t\t{notas[x]}\t\t{dataTexto}')
                print('_' * 58)

            OPC = str(input('\n[1] - Situação do Aluno\n[*] - Sair\n>>> '))

            if OPC != '1':
                clear()
                menu()
            else:
                calcularNotas(notas)


    #Calculando Notas
    def calcularNotas(notas):

        soma = 0.0

        for x in range(len(notas)):
            soma += notas[x]

        verificarSituacao(soma)            


    #Verificando a Situação do Aluno
    def verificarSituacao(value):

        if expiration == False:
            media = round(value / CALC, 1)

            print('')

            if media >= 7:
                print(f'Média: {media}')
                print('\n\033[1;32mAPROVADO!\033[m')

                OPC = str(input('\n[*] - Sair\n>>> '))

                clear()
                menu()

            elif media >= 3 and media < 7:
                print(f'Média: {media}')
                print('\n\033[1;33mRECUPERAÇÃO!\033[m')

                OPC = str(input('\n[1] - Realizar Prova Final\n[*] - Sair\n>>> '))

                if OPC != '1':
                    clear()
                    menu()
                else:

                    OPC = str(input('\nInforme o valor da Final\n>>> ').replace(',', '.'))

                    notas.append(float(OPC))

                    verificarFinal(notas, float(OPC))

            else:
                print(f'Média: {media}')
                print('\n\033[1;31mREPROVADO!\033[m')
        else:
            
            if validation:
                print('\n\033[1;32mAPROVADO NA FINAL!\033[m')

            else:
                print('\n\033[1;31mREPROVADO NA FINAL!\033[m')
            
            OPC = str(input('\n[*] - Sair\n>>> '))
            clear()
            menu()


    #Verificando nota Final
    def verificarFinal(notas, notaFinal):

        global validation, expiration

        if notaFinal != -1:
            soma = 0.0

            for x in range(len(notas)):
                soma += notas[x]

            media = round(((((soma - notaFinal) / CALC) * 6) + (notaFinal * 4)) / 10, 1)

            print('\n\033[1;32mCalculando média final...\033[m')
            time.sleep(2)

            clear()
            header()
            print(f'\nMédia Final: {media}')

            if media >= 5:
                print('\n\033[1;32mAPROVADO NA FINAL!\033[m')
                validation = True

            else:
                print('\n\033[1;31mREPROVADO NA FINAL!\033[m')
                validation = False
            
            expiration = True


            OPC = str(input('\n[*] - Sair\n>>> '))
            clear()
            menu()



    #Menu de Exibição
    def menu():
        clear()
        print('\n')
        header()
        print('\n[1] - Inserir Notas')
        print('[2] - Listar Notas')
        print('[3] - Sair')

        OPC = str(input('\n>>> '))

        if OPC == '1':
            clear()
            inserirNotas()
        elif OPC == '2':
            clear()
            listarNotas(notas)


    #Cabeçalho de Exibição
    def header():
        print('\n')
        print('=' * 58)
        print('=' * 19, ' Sistema de Notas ', '=' * 19)
        print('=' * 58)


    menu()

except (KeyboardInterrupt):
    print('\n\033[1;32mVolte Sempre\033[m')
