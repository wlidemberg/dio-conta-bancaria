import datetime
import pytz

menu  = """
[1] Depositar | [2] Sacar | [3] Extrato | [4] Sair\n
Digite a operação Desejada: \n
"""

saldo = []
depositos = []
saques = []
dt_transacoes = []
saldo_atual = 0
quantidade_saques = 0
quantidades_transacoes_diaria = 0
data_ultima_transacao = datetime.date.today()
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500
LIMITE_TRANSACAO_DIARIA = 5

def data_hora_atual():
  dt = datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')
  return dt

def efetuar_deposito(deposito:float):
  global quantidades_transacoes_diaria, saldo_atual
  if deposito > 0:
    if quantidades_transacoes_diaria < LIMITE_TRANSACAO_DIARIA:
      saldo.append(deposito)
      dt_transacoes.append(data_hora_atual())
      saldo_atual = sum(saldo)
      quantidades_transacoes_diaria+=1 
      return saldo_atual
    else:
      print(f"Você excedeu o limite de {LIMITE_TRANSACAO_DIARIA} por dia! Volte amanha!")
      return saldo_atual
  else:
    print('Não é possivel depositos zerados ou com valores negativos. Tente Novamente!')
    return saldo_atual

def efetuar_saque(saque, quantidade_saques):
  global quantidades_transacoes_diaria
  if quantidades_transacoes_diaria < LIMITE_TRANSACAO_DIARIA:
    if saque > 0 and saque <= LIMITE_SAQUE:
      if quantidade_saques < LIMITE_SAQUES:
        if saldo_atual > saque:
          saques.append(saque)
          dt_transacoes.append(data_hora_atual())
          quantidades_transacoes_diaria +=1
          return saque
        else:
          print('Saldo Insufuciente. Verifique valor disponível!')
          return 0
      else:
        print('Quantidade de saques por dia ultrapassado, volte amanha para relizar saques.') 
        return 0
    else:
      print(f'Valor do saque excedente, seu limite para saque é de R$ {LIMITE_SAQUE:.2f} por saque.')
      return 0
  else:
    print(f"Você excedeu o limite de {LIMITE_TRANSACAO_DIARIA} por dia! Volte amanha!")
    return 0
      
while True:
  data_do_dia = datetime.date.today()
  if data_do_dia > data_ultima_transacao:
    # Novo dia - zeramos o contador de transações
    quantidades_transacoes_diaria = 0
    data_ultima_transacao = data_do_dia

  if saldo_atual > 0:
    print('\n')
    print('-'*100)
    print(f'Saldo atual: R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques} | Transações Dia {quantidades_transacoes_diaria} | Data: {data_do_dia}')
    print('-'*100)
  else:
    print('-'*100)
    print(f'Saldo atual: R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques} | Transações Dia {quantidades_transacoes_diaria} | Data: {data_do_dia}')
    print('-'*100)

  operacao = input(menu)

  if operacao == '1':
    print('========== DEPOSITAR ==========\n')
    try:
      deposito = float(input('Digite o valor a ser depositado: '))
      valor_transacao = efetuar_deposito(deposito)
      saldo_atual = valor_transacao
      
    except ValueError:
      print('Entrada inválida, Digite apenas números!', ValueError)

  elif operacao == '2':
    try:
      print('========== SACAR ==========\n')
      if saldo_atual == 0:
        print('Não há saldo suficiente para realizar saques.')
        continue
      saque = float(input("Digite o valor a ser sacado: "))
      dados_saque = efetuar_saque(saque, quantidade_saques)
      saldo_atual = saldo_atual - dados_saque
      quantidade_saques +=1 if quantidade_saques < 3 else 0  
       
    except ValueError:
          print('Entrada inválida, Digite apenas números!', ValueError)

  elif operacao == '3':
    print('========== EXTRATO ==========\n')
    if len(saques) == 0 and len(saldo) == 0:
      print('Não houve movimentações nessa conta.')
      continue
    print('Depositos --------------------------------------------')
      
    for id, (valor, data) in enumerate(zip(saldo, dt_transacoes)):
      print(f"{id+1:2} {'-'*20} [+] R$ {valor:8.2f} - {data}")
      
    print('\nSaques ---------------------------------------------') 
    for id, (valor, data) in enumerate(zip(saques, dt_transacoes)):
      print(f"{id+1:<2} {'-'*20} [-] R$ {valor:8.2f} - {data}")
    
    print('-'*100)
    print('-'*100)
    print(f'Saldo atual ------------[+] R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques} | Transações efetuadas: {quantidades_transacoes_diaria}')
    
  elif operacao == '4':
    print('Sair')
    break
  else:
    print('Escolha uma opção válida.')