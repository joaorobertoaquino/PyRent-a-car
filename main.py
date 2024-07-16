import funcoes
import cliente
import funcionario

##########################################
#####  Locadora de Carros - Crystal  #####
#########################################
op_pric = ''
while op_pric != '0':
  op_pric = funcoes.menuPrincipal()
  
  if op_pric == '1':
    op_cliente = ''
    while op_cliente != '0':
      op_cliente = funcoes.modCliente()
      
      if op_cliente == '1':
        cliente.cadastrarCliente()
      elif op_cliente == '2':
        cliente.exibirDadosCliente()
      elif op_cliente == '3':
        cliente.alterarDadosCliente() 
      elif op_cliente == '4':
        cliente.excluirCliente()
  
  elif op_pric == '2':
    op_func = ''
    while op_func != '0':
      op_func = funcoes.modFunc()
      
      if op_func == '1':
        funcionario.cadastrarFunc()
      elif op_func == '2':
        funcionario.exibirDadosFunc()
      elif op_func == '3':
        funcionario.alterarDadosFunc()
      elif op_func == '4':
        funcionario.excluirFunc()

  elif op_pric == '3':
    op_veic = ''
    while op_veic != '0':
      op_veic = funcoes.modVeic()

      if op_veic == '1':
        funcoes.cadastrarVeic()
      elif op_veic == '2':
        funcoes.exibirDadosVeic()
      elif op_veic == '3':
        funcoes.alterarDadosVeic()
      elif op_veic == '4':
        funcoes.excluirVeic()

  elif op_pric == '4':
    op_reserva = ''
    while op_reserva != '0':
      op_reserva = funcoes.modReserva()
      
      if op_reserva == '1':
        funcoes.reservarVeiculo()
      elif op_reserva == '2':
        funcoes.devolverVeiculo()
      elif op_reserva == '3':
        funcoes.veiculosDisponiveis()
      elif op_reserva == '4':
        funcoes.veiculosAlugados()
      elif op_reserva == '5':
        funcoes.politicaCombustivel()

  elif op_pric == '5':
    op_relatorio = ''
    while op_relatorio != '0':
      op_relatorio = funcoes.modRelatorio()

      if op_relatorio == '1':
        funcoes.lista_geral_clientes()
      elif op_relatorio == '2':
        funcoes.lista_geral_funcionarios()
      elif op_relatorio == '3':
        funcoes.lista_geral_veiculos()
      elif op_relatorio == '4':
        funcoes.veiculos_mais_procurados()
      elif op_relatorio == '5':
        funcoes.historicoAlugueis()

  elif op_pric == '6':
    op_pric = funcoes.modInfo()

print("\nAté logo!")
funcoes.escreverArquivos()

