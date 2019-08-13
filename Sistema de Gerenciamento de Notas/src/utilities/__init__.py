try:
    # Imports de bibliotecas
    import os
    import time

    # Variáveis Globais

    turma = list()
    alunos = dict()
    notas = list()

    op = ''


    # Limpar Terminal

    def Clear():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")


    def ListNotes():

        # Verificando se o dicionario está vazio
        if turma != []:

            Clear()
            Header()
            print()
            print(' ID ', end='')

            # Exibi os Headers da Tabela
            for i in alunos.keys():
                print(f'{i:^17}', end='')
            print()
            print('_' * 50)

            print()

            for indice, j in enumerate(turma):
                turma[indice]['Media'] = round(turma[indice]['Media'], 1)
                # Exibi os IDs
                print(f'{indice:^4} ', end='')
                # Exibi os valores
                for dado in j.values():
                    print(f'{str(dado):^16}', end='')
                print()
                print('_' * 50)

            print()

            while True:
                print()
                try:
                    busca = int(input('Informe o ID para exibir os dados\n[999] - Sair\n>>> '))

                    if busca == 999:
                        Menu()
                        break
                    if busca >= len(turma):
                        print('\nErro')
                    else:
                        Clear()
                        Header()
                        print('\n')
                        print('=' * 52)
                        print('=' * 14, f'Dados do Aluno, {turma[busca]["Nome"]}', 13 * '=')
                        print()

                        for indice, notas in enumerate(turma[busca]['Notas']):
                            print(f'     Na {indice + 1}ª avalição, fez {notas} pontos')

                        print('\n\t Média Final: {}'.format(round(turma[busca]["Media"], 2)))

                        if turma[busca]['Media'] >= 7:
                            print('\t\033[1;32m APROVADO!\033[m')

                        elif (turma[busca]['Media'] >= 3) and (turma[busca]['Media'] < 7):

                            print('\t\033[1;33m RECUPERAÇÃO!\033[m')

                            print(f'\t\nNota necessária para passar na Final {14 - turma[busca]["Media"]}')

                            op = input('\n[1] - Realizar a Prova Final\n[*] - Sair\n>>> ')

                            if op == '1':

                                entrada = float(input('\nInforme a nota: '))

                                # Alterando Média
                                for i in enumerate(turma[busca]):
                                    soma = (entrada + turma[busca]['Media']) / 2

                                    if soma >= turma[busca]['Media']:
                                        turma[busca]['Media'] = 0  # Q - Segurança
                                        turma[busca]['Media'] = soma

                                    break

                        else:
                            print('\t\033[1;31m REPROVADO!\033[m')

                        op = str(input('\n[*] - Sair\n>>> '))

                        if op == '*' or op != '*':
                            Clear()
                            Menu()
                            break

                except (ValueError, TypeError):
                    print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')

        else:
            Clear()
            Header()
            print('\n\033[1;31mNENHUM ALUNO OU NOTAS FORAM INSERIDAS!!\033[m')
            time.sleep(2)

            opc = str(input('\n[1] - Inserir notas\n[*] - Sair\n>>> '))

            if opc == '1':
                Clear()
                InsertNotes()
            else:
                Clear()
                Menu()


    # Inserindo Notas
    def InsertNotes():

        Header()
        
        while True:
            soma = 0.0
            print()
            alunos.clear()
            try:

                alunos['Nome'] = str(input('Informe o Primeiro nome do Aluno: ').title())

                if alunos['Nome'] == '':
                    alunos.clear()
                    Menu()

                if alunos['Nome'].isalpha():
                    print()
                    tot = int(input(f'Quantas avaliações feitas pelo {alunos["Nome"]}?\n>>> '))
                    notas.clear()

                    print()
                    for c in range(0, tot):
                        try:
                            entrada = str(input(f'     Valor da {c + 1}º avaliação: ')).replace(',', '.')
                            value = float(entrada)
                            arredondar = round(value, 1)
                            notas.append(float(arredondar))

                        except (ValueError, TypeError):
                            print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')
                            Menu()

                    alunos['Notas'] = notas[:]
                    soma = sum(notas)
                    alunos['Media'] = soma / 2

                    turma.append(alunos.copy())

                    print()
                else:
                    print('', end='')
                    print(f'\033[1;31mO valor\033[m {alunos["Nome"]} \033[1;31mé inválido\033[m')

            except (ValueError, TypeError):
                print('\n\033[1;33mTivemos um erro nos tipos de dados que você digitou!\033[m')

            except KeyboardInterrupt:
                print('\n\033[1;33mO usuário não informou os dados\033[m')

            while True:
                resp = str(input('Quer continuar?\n>>> '))
                print()
                Clear()
                if resp in 'sn':
                    break
            if resp == 'n':
                Menu()
                break
            Clear()


    def Opc(opc):
        if opc == '1':
            Clear()
            InsertNotes()
        elif opc == '2':
            Clear()
            ListNotes()
        else:

            Menu()


    # Cabeçalho
    def Menu():
        Header()
        print("\n[1] - Cadastrar Aluno e Inserir Notas")
        print("[2] - Listar Notas")
        print("[*] - Sair")

        opc = str(input("\n>>> "))

        Opc(opc)


    def Header():
        print("\n")
        print("==" * 26)
        print("==" * 8, " Sistema de Notas ", "==" * 8)

except KeyboardInterrupt:
    print('\nO usuário não informou os dados')
