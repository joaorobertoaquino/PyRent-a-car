import os

########################################################
#####                Menu Pricipal                 #####
########################################################
def menuPrincipal():
    os.system("clear")
    print("############################################")
    print("######      Locadora de Carros        ######")
    print("############################################")
    print("#####      1 - Módulo Cliente          #####")
    print("#####      2 - Módulo Funcionários     #####")
    print("#####      3 - Módulo Veículos         #####")
    print("#####      4 - Módulo Reserva          #####")
    print("#####      5 - Módulo Relatório        #####")
    print("#####      6 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    op_pric = input("##### Escolha sua opção: ")
    return op_pric
    
###############################################  
#####          Módulo Cliente             #####  
############################################### 
cliente = {
  '22233344455': ['Taciano Silva', 'taciano@ufrn.br', '(83) 99900-0111'], 
  '33344455566': ['Karliane Vale', 'karliane@ufrn.br', '(84) 99999-8888'],
  '44455566677': ['João Roberto', 'joao@ufrn.br', '(84) 99801-1505']
}

def modCliente():
    os.system("clear")
    print()
    print("#############################################")
    print("#####    Você está no Módulo Cliente    #####")
    print("#############################################")
    print("##### 1 - Cadastrar Cliente             #####")
    print("##### 2 - Exibir Dados do Cliente       #####")
    print("##### 3 - Alterar Dados do Cliente      #####")
    print("##### 4 - Excluir Cliente               #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_cliente = input("##### Escolha sua opção: ") 
    return op_cliente

def cadastrarCliente():
    os.system("clear")
    print()
    print("#############################################")
    print("#####        Cadastrar Cliente         #####")
    print("#############################################")
    print()
    nome = input("##### Nome: ")
    print()
    cpf = input("##### CPF: ")
    print()
    email = input("##### Email: ")
    print()
    fone = input("##### Celular: ")
    print()
    cliente[cpf] = [nome,email,fone]
    print(cliente)
    print("Aluno cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosCliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####     Exibir Dados do Cliente      #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do cliente?')
    if cpf in cliente:
        print("##### Nome: ", cliente[cpf][0])
        print("##### CPF: ", cpf)
        print("##### Email: ", cliente[cpf][1])
        print("##### Celular: ", cliente[cpf][2])
    else:
        print('Cliente inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosCliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####      Alterar Dados do Cliente    #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do cliente?')
    if cpf in cliente:
        print('Informe os novos dados do cliente: ')
        nome = input("##### Nome: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        cliente[cpf] = [nome,email,fone]
        print("Dados alterados com sucesso!")
    else:
        print('Cliente inexistente!')
    input("Tecle <ENTER> para continuar...")

def excluirCliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Excluir Cliente          #####")
    print("############################################")
    print()
    cpf = input('Informe o CPF do cliente: ')
    if cpf in cliente:
        print("##### Nome: ", cliente[cpf][0])
        print("##### Email: ", cliente[cpf][1])
        print("##### Celular: ", cliente[cpf][2])
        print()
        resp = input('Tem certeza que deseja excluir este cliente? (S/N)?')
        if resp.upper() == 'S':
            del cliente[cpf]
            print("Aluno excluído com sucesso!")
        else:
            print('Exclusão não realizada!')
    else:
        print('Cliente inexistente!')
    input("Tecle <ENTER> para continuar...")
    
############################################### 
#####          Módulo Funcionários        #####        
###############################################    
funcionarios = {
  '11122233344': ['Flavius Gorgônio', 'flavius@ufrn.br', '(84) 99988-8777'], 
  '22233344455': ['Taciano Silva', 'taciano@ufrn.br', '(83) 99900-0111'], 
  '33344455566': ['Karliane Vale', 'karliane@ufrn.br', '(84) 99999-8888']
}

def modFunc():
    os.system("clear")
    print()
    print("#############################################")
    print("##### Você está no Módulo Funcionários  #####")
    print("#############################################")
    print("##### 1 - Cadastrar Funcionários        #####")
    print("##### 2 - Exibir Dados do Funcionários  #####")
    print("##### 3 - Alterar Dados do Funcionários #####")
    print("##### 4 - Excluir Funcionário           #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_func = input("##### Escolha sua opção: ")
    return op_func

def cadastrarFunc():
    os.system("clear")
    print()
    print("#############################################")
    print("#####      Cadastrar Funcionário        #####")
    print("#############################################")
    print()
    nome = input("##### Nome: ")
    print()
    cpf = input("##### CPF: ")
    print()
    email = input("##### Email: ")
    print()
    fone = input("##### Celular: ")
    print()
    funcionarios[cpf] = [nome,email,fone]
    print(funcionarios)
    print("Funcionário cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosFunc():
    os.system("clear")
    print()
    print("############################################")
    print("#####   Exibir Dados do Funcionário    #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do funcionário(a)? ')
    if cpf in funcionarios:
        print("##### Nome: ", funcionarios[cpf][0])
        print("##### CPF: ", cpf)
        print("##### Email: ", funcionarios[cpf][1])
        print("##### Celular: ", funcionarios[cpf][2])
    else:
        print('Funcionário(a) inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosFunc():
    os.system("clear")
    print()
    print("############################################")
    print("#####   Alterar Dados do Funcionário   #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do funcionário(a)? ')
    if cpf in funcionarios:
        print('Informe os novos dados do funcionário(a): ')
        nome = input("##### Nome: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        funcionarios[cpf] = [nome,email,fone]
        print('Dados alterados com sucesso!')
    else:
        print('Funcionário(a) inexistente!')
    input("Tecle <ENTER> para continuar...")

def excluirFunc():
    os.system("clear")
    print()
    print("############################################")
    print("#####       Excluir Funcionário        #####")
    print("############################################")
    print()
    cpf = input('Informe o CPF do funcionário(a): ')
    if cpf in funcionarios:
        print("##### Nome: ", funcionarios[cpf][0])
        print("##### Email: ", funcionarios[cpf][1])
        print("##### Celular: ", funcionarios[cpf][2])
        print()
        resp = input('Tem certeza que deseja excluir este funcionário(a)? (S/N)')
        if resp.upper() == 'S':
            del funcionarios[cpf]
            print("Funcionário(a) excluído com sucesso!")
        else:
            print('Exclusão não realizada!')
    else:
        print("Funcionário inexistente!")
    input("Tecle <ENTER> para continuar...") 

###########################################
#####         Módulo Veículos         #####         
###########################################
veiculos = {
    'BEE4R22': ['Chevrolet', 'Onix', '2020', 'Branco'],
    'AAA2T33': ['Chevrolet', 'Onix Plus', '2020', 'Vermelho'],
    'BBB3E44': ['Ferrari', 'Ferrari 488 GTB', '2022', 'Branco']
}

def modVeic():
    os.system('clear')    
    print()
    print("############################################")
    print("#####         Módulo Veículos          #####")
    print("############################################")
    print("##### 1 - Cadastrar Veículo            #####")
    print("##### 2 - Exibir Dados do Veículo      #####")
    print("##### 3 - Alterar Dados do Veículo     #####")
    print("##### 4 - Excluir Veículo              #####")
    print("##### 0 - Retornar ao Menu Principal   #####")
    op_veic = input("##### Escolha sua opção: ")
    return op_veic

def cadastrarVeic():
    os.system('clear')
    print()
    print("############################################")
    print("#####        Cadastrar Veículo         #####")
    print("############################################")
    print()
    marca = input("##### Marca: ")
    print()
    modelo = input("##### Modelo: ")
    print()
    ano = input("##### Ano de lançamento: ")
    print()
    cor = input("##### Cor: ")
    print()
    placa = input("##### Número da placa: ")
    print()
    veiculos[placa] = [marca,modelo,ano,cor]
    print(veiculos)
    print("Veículo cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosVeic():
    os.system('clear')
    print()
    print("############################################")
    print("#####    Exibir Dados do Veículo       #####")
    print("############################################")
    print()
    placa = input('Informe a placa do veículo? ')
    if placa in veiculos:
        print("##### Marca: ", veiculos[placa][0])
        print("##### Modelo: ", veiculos[placa][1])
        print("##### Ano de lançamento: ", veiculos[placa][2])
        print("##### Cor: ", veiculos[placa][3])
        print("##### Número da placa: ", placa)
    else:
        print('Veículo inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosVeic():
    os.system('clear')
    print()
    print("############################################")
    print("#####    Alterar Dados do Veículo      #####")
    print("############################################")
    print()
    placa = input('Informe a placa do veículo: ')
    if placa in veiculos:
        print('Informe os novos dados do veículo: ')
        marca = input("##### Marca: ")
        print()
        modelo = input("##### Modelo: ")
        print()
        ano = input("##### Ano de lançamento: ")
        print()
        cor = input("##### Cor: ")
        print()
        veiculos[placa] = [marca,modelo,ano,cor]
        print("Dados alterados com sucesso!")
    else:
        print('Veículo inexistente!')
    input("Tecle <ENTER> para continuar...")

def excluirVeic():
    os.system('clear')
    print()
    print("############################################")
    print("#####       Excluir Veículo            #####")
    print("############################################")
    print()
    placa = input('Informe a placa do veículo: ')
    if placa in veiculos:
        print("##### Marca: ", veiculos[placa][0])
        print("##### Modelo: ", veiculos[placa][1])
        print("##### Ano de lançamento: ", veiculos[placa][2])
        print("##### Cor: ", veiculos[placa][3])
        print()
        resp = input('Tem certeza que deseja excluir este veículo? (S/N)')
        if resp.upper() == 'S':
            del veiculos[placa]
            print("Veículo excluído com sucesso!")
        else:
            print('Exclusão não realizada!')
    else:
        print('Veículo inexistente!')
    input("Tecle <ENTER> para continuar...")

############################################
#####          Módulo Reserva          #####        
############################################
def modReserva():
    os.system('clear')
    print()
    print("#############################################")
    print("#####   Você está no Módulo Reserva     #####")
    print("#############################################")
    print("##### 1 - Lista de Veículos Disponíveis #####")
    print("##### 2 - Opções de Seguro              #####")
    print("##### 3 - Formas de Pagamento           #####")
    print("##### 4 - Política de Combustível       #####")
    print("##### 5 - Suporte ao Cliente            #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_reserva = input("##### Escolha sua opção: ")
    return op_reserva

#############################################
#####         Módulo Relatório          #####   
#############################################
def modRelatorio():
    os.system('clear')
    print()
    print("#############################################")
    print("#####   Você está no Módulo Relatório   #####")
    print("#############################################")
    print("##### 1 - Lista Geral de Funcionários   #####")
    print("##### 2 - Lista Geral de Veículos       #####")
    print("##### 3 - Lista de Veículos Alugados    #####")
    print("##### 4 - Veículos mais Procurados      #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_relatorio = input("##### Escolha sua opção: ")
    return op_relatorio 

   
##############################################
#####         Módulo Informações         #####    
##############################################
def modInfo():
    os.system('clear')
    print()
    print("#############################################")
    print("#####  Você está no Módulo Informações  #####")
    print("#############################################")
    print("##### Projeto   -  Locadora de Veículos #####")
    print("##### Desenvolvimento:                  #####")
    print("##### João Roberto Galvão Aquino        #####")
    print("##### E-mail para comunicação:          #####")
    print("##### joao.roberto.galvao.017@gmail.com #####")
    print()
    input("Tecle <ENTER> para voltar ao menu principal...")