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
        valor = float(input("Informe o valor para depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falho! O valor informado é invalido")
    elif opcao == "s":
        
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = num_saques >= LIMITE_SAQUES
        
        
        if excedeu_saldo:
            print("Saldo insulficiente")
        if excedeu_limite:
            print("Valor do saque não permitido")
        if excedeu_saque:
            print("Numéro de saque atingido por hoje")   
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor: .2f}\n"
            num_saques += 1
        else:
            print("Operação falho! O valor informado é invalido")



    elif opcao == "e":
        print("\n===========EXTRATO==========")
        print("Não foram encontradas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo: .2f}")
        print("==============================")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

