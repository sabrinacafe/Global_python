def opcao_user():
    acao = True

    while acao:
        print('Bem vindo ao Menu Hapvida')
        print('1. Categorias')
        print('2. Agenda')
        print('3. Empresa')
        print('4. Cadastro')
        print('5. Suporte')
        print('6. Sair')

        opcao_user = input('Selecione uma opção: ')

        if opcao_user.isdigit() and 1 <= int(opcao_user) <8:
            if opcao_user == '1':
                opcao_categorias()
            elif opcao_user == '2':
                opcao_agenda()
            elif opcao_user == '3':
                opcao_empresa()
            elif opcao_user == '4':
                opcao_cadastro()
            elif opcao_user == '5':
                opcao_suporte()
            elif opcao_user == '6':
                acao = False
                print('Saindo do programa. Volte sempre!')
            else:
                print('Opção inválida, digite novamente')
        else:
            print('Opção inválida, digite novamente')