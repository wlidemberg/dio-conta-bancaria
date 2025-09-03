menu  = """
[1] Depositar | [2] Sacar | [3] Extrato | [4] Sair\n
Digite a operação Desejada: \n
"""

saldo = []
depositos = []
saques = []
saldo_atual = 0
quantidade_saques = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

while True:



  if saldo_atual > 0:
    print('\n')
    print('-'*100)
    print(f'Saldo atual: R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques}')
    print('-'*100)
  else:
    print('-'*100)
    print(f'Saldo atual: R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques}')
    print('-'*100)

  operacao = input(menu)

  if operacao == '1':
    print('========== DEPOSITAR ==========\n')
    try:
      deposito = float(input('Digite o valor a ser depositado: '))
      if deposito > 0:
        saldo.append(deposito)
        saldo_atual = sum(saldo)
      else:
        print('Não é possivel depositos zerados ou com valores negativos. Tente Novamente!')
    except ValueError:
      print('Entrada inválida, Digite apenas números!', ValueError)

  elif operacao == '2':
    try:
      print('========== SACAR ==========\n')
      if saldo_atual == 0:
        print('Não há saldo suficiente para realizar saques.')
        continue
      saque = float(input("Digite o valor a ser sacado: "))
      saques.append(saque)
      if saque > 0 and saque <= LIMITE_SAQUE:
        if quantidade_saques < LIMITE_SAQUES:
          if saldo_atual >= saque:
            saldo_atual = saldo_atual - saque
            quantidade_saques += 1
            print(f"Saque de R$ {saque:.2f} autorizado, ")
          else:
            print('Saldo Insufuciente. Verifique valor disponível!')
        else:
          print('Quantidade de saques por dia ultrapassado, volte amanha para relizar saques.')
      else:
        print(f'Valor do saque excedente, seu limite para saque é de R$ {LIMITE_SAQUE:.2f} por saque.')
    except ValueError:
      print('Entrada inválida, Digite apenas números!', ValueError)

  elif operacao == '3':
    print('========== EXTRATO ==========\n')
    if len(saques) == 0 and len(saldo) == 0:
      print('Não houve movimentações nessa conta.')
      continue
    print('Depositos --------------------------------------------')  
    for id,  valor in enumerate(saldo):
      contar = str(valor)
      if len(contar) == 7:
        print(f'{id+1} ----------------------[+] R$ {valor:.2f}')
      elif len(contar) == 6:
        print(f'{id+1} ----------------------[+] R$  {valor:.2f}')
      elif len(contar) == 5:
        print(f'{id+1} ----------------------[+] R$   {valor:.2f}')
      elif len(contar) == 4:
        print(f'{id+1} ----------------------[+] R$    {valor:.2f}')
      elif len(contar) == 3:
        print(f'{id+1} ----------------------[+] R$     {valor:.2f}')    

    print('\nSaques ---------------------------------------------') 
    for id, valor in enumerate(saques):
      contar = str(valor)        
      if len(contar) == 7:
        print(f'{id+1} ----------------------[-] R$ {valor:.2f}')
      elif len(contar) == 6:
        print(f'{id+1} ----------------------[-] R$  {valor:.2f}')
      elif len(contar) == 5:
        print(f'{id+1} ----------------------[-] R$   {valor:.2f}')
      elif len(contar) == 4:
        print(f'{id+1} ----------------------[-] R$    {valor:.2f}')
      elif len(contar) == 3:
        print(f'{id+1} ----------------------[-] R$     {valor:.2f}')  
    print('-'*100)
    print('-'*100)
    print(f'Saldo atual ------------[+] R$ {saldo_atual:.2f} | Saques realizados no dia {quantidade_saques}')
    
  elif operacao == '4':
    print('Sair')
    break
  else:
    print('Escolha uma opção válida.')