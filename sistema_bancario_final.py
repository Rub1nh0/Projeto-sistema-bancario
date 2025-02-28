menu = """

[d]Depósito
[s]Saque
[e]Extrato
[q]Sair

"""

saldo = 0 
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3
JUROS_CHEQUE_ESPECIAL = 0.02  # 2% de juros
cheque_especial = 300  # Limite do cheque especial

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor para depósito: "))
            if valor > 0:
                if cheque_especial < 300:

                    dep_no_cheque_esp = 300 - cheque_especial
                    dep_na_conta = valor - dep_no_cheque_esp
                    
                    cheque_especial += dep_no_cheque_esp
                    saldo += dep_na_conta
                    extrato += f"Depósito: R${dep_no_cheque_esp: .2f} no cheque especial e R${dep_na_conta: .2f} na conta\n"
                else:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor: .2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Você deve digitar um número válido.")


    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = num_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Saldo insuficiente.")
                usar_cheque_especial = input(f"Você deseja utilizar o cheque especial ({JUROS_CHEQUE_ESPECIAL * 100: .1f}% de juros)? [s/n]: ")
                
                if usar_cheque_especial.lower() == "s":
                    # Cheque especial só pode ser usado até o limite de R$ 300
                    saldo_com_cheque_especial = saldo + cheque_especial
                    
                    if valor <= saldo_com_cheque_especial:
                        juros = valor * JUROS_CHEQUE_ESPECIAL
                        valor_com_juros = valor + juros
                        print(f"Você usará o cheque especial. O valor do saque com juros será: R$ {valor_com_juros: .2f} (juros de R$ {juros: .2f}).")
                        
                        saldo -= valor_com_juros
                        cheque_especial -= valor_com_juros
                        extrato += f"Saque com cheque especial: R$ {valor_com_juros: .2f} (juros: R$ {juros: .2f})\n"
                        num_saques += 1
                    elif cheque_especial > 0:
                        juros = valor * JUROS_CHEQUE_ESPECIAL
                        valor_com_juros = valor + juros
                        print(f"Você usará o cheque especial. O valor do saque com juros será: R$ {valor_com_juros: .2f} (juros de R$ {juros: .2f}).")
                        
                        saldo -= valor_com_juros
                        cheque_especial -= valor
                        extrato += f"Saque com cheque especial: R$ {valor_com_juros: .2f} (juros: R$ {juros: .2f})\n"
                        num_saques += 1

                    else:
                        print(f"\nO valor total (saque + juros) excede o limite do cheque especial (R$ {cheque_especial: .2f}).")
                elif usar_cheque_especial.lower() == "n":
                    print("Você optou por não usar o cheque especial.")
                else:
                    print("Operação falhou! O valor informado é inválido.")   
        
            elif excedeu_limite:
                print("Valor do saque não permitido.")
            elif excedeu_saque:
                print("Número de saques atingido por hoje.")   
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: .2f}\n"
                num_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Você deve digitar um número válido.")

            
    elif opcao == "e":
        print("\n===========EXTRATO==========")
        print("Não foram encontradas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print(f"\nValor Cheque Especial: R$ {cheque_especial: .2f}")
        print("==============================")
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
