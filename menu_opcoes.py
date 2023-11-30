pacientes = []
fisioterapeutas = []

def opcao_user():
    while True:
        print('Bem vindo ao Menu Hapvida')
        print('1. Categorias')
        print('2. Agenda')
        print('3. Empresa')
        print('4. Cadastro')
        print('5. Suporte')
        print('6. Sair')

        select_user = input('Selecione uma opção: ')

        if select_user.isdigit() and 1 <= int(select_user) <8:
            if select_user == '1':
                opcao_categorias()
            elif select_user == '2':
                opcao_agenda()
            elif select_user == '3':
                opcao_empresa()
            elif select_user == '4':
                opcao_cadastro()
            elif select_user == '5':
                opcao_suporte()
            elif select_user == '6':
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

        if select_categoria == '9':
            print('Voltando ao Menu Inicial')
            break
        elif select_categoria.isdigit() and 1 <= int(select_categoria) <= 8:
            exibir_info_categoria(select_categoria)
        else:
            print('Opção inválida')

def exibir_info_categoria(categoria):
    categorias_info = {
        '1': 'Quiropraxia é uma abordagem de saúde que trata problemas musculoesqueléticos, especialmente na coluna vertebral, usando ajustes manuais. Busca aliviar dores e melhorar a função do sistema nervoso.',
        '2': 'Massoterapia é uma prática terapêutica que envolve a aplicação de técnicas de massagem para promover relaxamento, alívio de tensões musculares e melhorar o bem-estar físico e emocional. Ela é utilizada para reduzir o estresse, aliviar dores musculares, melhorar a circulação sanguínea e promover a saúde geral.',
        '3': 'Fisioterapia respiratória é uma especialidade da fisioterapia que visa tratar e prevenir distúrbios respiratórios. Utiliza técnicas e exercícios para melhorar a função pulmonar, facilitar a respiração e ajudar pacientes com condições como asma, doença pulmonar obstrutiva crônica (DPOC) e outras doenças respiratórias.',
        '4': 'Dores nas costas podem ser causadas por diversos fatores. Agende com um de nossos especialistas para que ele possa indicar a melhor forma de tratamento.',
        '5': 'A fisioterapia pediátrica é uma especialidade que trata crianças, utilizando técnicas e exercícios específicos para promover o desenvolvimento motor, melhorar a função física e tratar condições pediátricas como atrasos no desenvolvimento, lesões neuromusculares e problemas ortopédicos. Ela visa melhorar a qualidade de vida e a independência funcional das crianças.',
        '6': 'O tratamento com ventosas é uma técnica terapêutica que envolve a aplicação de copos de sucção na pele para criar pressão negativa. Isso promove o aumento do fluxo sanguíneo local, alivia a tensão muscular e pode ser usado para tratar dores musculares, melhorar a circulação e promover a recuperação de lesões.',
        '7': 'A fisioterapia geriátrica é uma especialidade que se concentra no tratamento de idosos, visando melhorar a mobilidade, equilíbrio, força e independência funcional. Ela ajuda a prevenir e tratar condições relacionadas à idade, promovendo a qualidade de vida e a autonomia dos idosos.',
        '8': 'Reabilitação vestibular é um conjunto de exercícios e técnicas utilizados para tratar distúrbios do sistema vestibular, que controla o equilíbrio e a orientação espacial. Essa terapia é empregada para aliviar tonturas, vertigens e problemas de equilíbrio, visando melhorar a função vestibular e a qualidade de vida do paciente.'
    }

    print(categorias_info.get(categoria, 'Opção inválida'))

def opcao_agenda():
    while True:
        print('Você selecionou Agenda, o que deseja saber ?: ')
        print('1. Acessar histórico de consultas')
        print('2. Acessar consultas futuras')
        print('3. Acessar todas as consultas')
        print('4. Voltar ao Menu Inicial')

        select_agenda = input('Digite a opção desejada: ')
        if select_agenda == '1':
            exibir_historico_consultas()
        elif select_agenda == '2':
            exibir_consultas_futuras()
        elif select_agenda == '3':
            exibir_todas_consultas()
        elif select_agenda == '4':
            print('Voltando ao Menu inicial...')
            return
        else:
            print('Opção inválida')

def exibir_historico_consultas():
    if not pacientes:
        print('Nenhum paciente cadastrado.')
        return

    for paciente in pacientes:
        print(f"Nome: {paciente['Nome']}, Histórico de Consultas: ...")

def exibir_consultas_futuras():
    if not pacientes:
        print('Nenhum paciente cadastrado.')
        return

    for paciente in pacientes:
        print(f"Nome: {paciente['Nome']}, Consultas Futuras: ...")

def exibir_todas_consultas():
    if not pacientes:
        print('Nenhum paciente cadastrado.')
        return

    for paciente in pacientes:
        print(f"Nome: {paciente['Nome']}, Todas as Consultas: ...")

def opcao_empresa():
    while True:
        print('Você selecionou Empresa, qual a informação gostaria de visitar?: ')
        print('1. Quem é a Hapvida')
        print('2. Nossa Missão com a Fisioterapia à Domicilio')
        print('3. Localização da Sede')
        print('4. Voltar ao Menu Inicial')

        select_empresa = input('Digite a opção desejada: ')
        if select_empresa == '1':
            print('A Hapvida NotreDame Intermédica é, hoje, a maior operadora de saúde do Brasil')
        elif select_empresa == '2':
            print('Proporcionar saúde integrada de qualidade, acessível a geração de brasileiros.')
        elif select_empresa == '3':
            print('Av. Heráclito Graça, 406 Centro - CEP 60140-061 Fortaleza-CE')
        elif select_empresa== '4':
            print('Voltando ao Menu inicial...')
            break
        else:
            print('Opção inválida')

def cadastrar_paciente():
    print('Cadastro de Paciente')
    nome = input('Nome: ')
    idade = input('Idade: ')
    endereco = input('Endereço: ')
    cpf = input('CPF: ')
    email = input('E-mail: ')
    telefone_paciente = input('Telefone: ')
    motivo_consulta = input('Motivo da Consulta: ')

    paciente = {
        'Nome': nome,
        'Idade': idade,
        'Endereço': endereco,
        'CPF': cpf,
        'E-mail': email,
        'Telefone': telefone_paciente,
        'Motivo da Consulta': motivo_consulta
    }

    pacientes.append(paciente)
    print('Cadastro realizado com sucesso!')

def cadastrar_fisioterapeuta():
    print('Cadastro de Fisioterapeuta')
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    cpf_cnpj = input('CPF ou CNPJ: ')
    email = input('E-mail: ')
    telefone_fisioterapeuta = input('Telefone: ')
    especialidade = input('Especialidade: ')

    fisioterapeuta = {
        'Nome': nome,
        'Endereço': endereco,
        'CPF': cpf_cnpj,
        'E-mail': email,
        'Telefone': telefone_fisioterapeuta,
        'Especialidade': especialidade
    }

    fisioterapeutas.append(fisioterapeuta)
    print('Cadastro realizado com sucesso!')

def opcao_cadastro():
    while True:
        print('Você selecionou Cadastro: ')
        print('1. Você é um paciente')
        print('2. Você é um fisioterapeuta')
        print('3. Voltar ao Menu Inicial')

        select_cadastro = input('Selecione uma opção: ')

        if select_cadastro == '1':
            cadastrar_paciente()
        elif select_cadastro == '2':
            cadastrar_fisioterapeuta()
        elif select_cadastro == '3':
            print('Voltando ao Menu inicial...')
            break
        else:
            print('Opção inválida')


def opcao_suporte():
    while True:
        print('Você selecionou Suporte: ')
        print('1. Atendimento Telefonico')
        print('2. Atendimento por email')
        print('3. Atendimento Online')
        print('4. Voltar ao Menu Inicial')

        select_suporte = input('Digite a opção desejada: ')
        if select_suporte == '1':
            print('Ligue para o Call Center 24h 4002.3633, 4020.3633 ou 0300 313 3633')
        elif select_suporte == '2':
            print('Mande sua dúvida para o email: fisioterapia@hapvida.com.br')
        elif select_suporte == '3':
            print('Acesse nosso Chatbot localizado no cando inferior direito do site')
        elif select_suporte == '4':
            print('Voltando ao Menu inicial...')
            break
        else:
            print('Opção inválida')

opcao_user()
