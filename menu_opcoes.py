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

def opcao_categorias():
    while True:
        print('Você selecionou Categorias. Qual especialidade você deseja saber mais ?: ')
        print('1. Quiropraxia')
        print('2. Massoterapia')
        print('3. Fisioterapia Respiratória')
        print('4. Dores na coluna')
        print('5. Fisioterapia Pediátrica')
        print('6. Ventosa')
        print('7. Fisioterapia Melhor Idade')
        print('8. Reabilitação Vestibular')
        print('9. Voltar ao Menu Inicial')

        select_categoria = input('Selecione uma opção: ')

        if select_categoria == '1':
            if select_categoria == '1':
                print('''
                   Quiropraxia é uma abordagem de saúde que trata problemas musculoesqueléticos,
                   especialmente na coluna vertebral, usando ajustes manuais. Busca aliviar dores
                   e melhorar a função do sistema nervoso.
                   ''')
            elif select_categoria == '2':
                print('''
                   Massoterapia é uma prática terapêutica que envolve a aplicação de técnicas
                   de massagem para promover relaxamento, alívio de tensões musculares e melhorar
                   o bem-estar físico e emocional. Ela é utilizada para reduzir o estresse, aliviar
                   dores musculares, melhorar a circulação sanguínea e promover a saúde geral.
                   ''')
            elif select_categoria == '3':
                print('''
                    Fisioterapia respiratória é uma especialidade da fisioterapia que visa tratar
                    e prevenir distúrbios respiratórios. Utiliza técnicas e exercícios para melhorar
                    a função pulmonar, facilitar a respiração e ajudar pacientes com condições como
                    asma, doença pulmonar obstrutiva crônica (DPOC) e outras doenças respiratórias.
                    ''')
            elif select_categoria == '4':
                print(
                    'Dores nas costas podem ser causadas por diversos fatores. Agende com um de nossos especialistas para que ele possa indicar a melhor forma de tratamento.')
            elif select_categoria == '5':
                print('''
                    A fisioterapia pediátrica é uma especialidade que trata crianças, utilizando
                    técnicas e exercícios específicos para promover o desenvolvimento motor, melhorar
                    a função física e tratar condições pediátricas como atrasos no desenvolvimento,
                    lesões neuromusculares e problemas ortopédicos. Ela visa melhorar a qualidade de vida
                    e a independência funcional das crianças.
                    ''')
            elif select_categoria == '6':
                print('''
                    O tratamento com ventosas é uma técnica terapêutica que envolve a aplicação de
                    copos de sucção na pele para criar pressão negativa. Isso promove o aumento do
                    fluxo sanguíneo local, alivia a tensão muscular e pode ser usado para tratar dores
                    musculares, melhorar a circulação e promover a recuperação de lesões.
                    ''')
            elif select_categoria == '7':
                print('''
                    A fisioterapia geriátrica é uma especialidade que se concentra no tratamento de
                    idosos, visando melhorar a mobilidade, equilíbrio, força e independência funcional.
                    Ela ajuda a prevenir e tratar condições relacionadas à idade, promovendo a qualidade
                    de vida e a autonomia dos idosos.
                    ''')
            elif select_categoria == '8':
                print('''
                    Reabilitação vestibular é um conjunto de exercícios e técnicas utilizados para tratar
                    distúrbios do sistema vestibular, que controla o equilíbrio e a orientação espacial. Essa
                    terapia é empregada para aliviar tonturas, vertigens e problemas de equilíbrio, visando
                    melhorar a função vestibular e a qualidade de vida do paciente.
                    ''')
            elif select_categoria == '9':
                print('Voltando ao Menu Inicial')
                break
            else:
                print('Opção inválida')