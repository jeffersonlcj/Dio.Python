menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"DEPOSITO: R$: {valor_deposito:.2f} \n"
    elif opcao == "s":
        if numero_saques>=LIMITE_SAQUES:
            print("Você excedeu o limite de saques diarios!")
        elif saldo > 0:
            valor_saque = float (input("Digite o valor a ser sacado: "))
            if valor_saque > limite:
                print("Valor maximo para saque R$: 500,00, refaça a operação")
            elif valor_saque<= saldo:
                saldo -= valor_saque
                extrato += f"SAQUE: R$: {valor_saque:.2f} \n"
                numero_saques += 1
            else:
                print("valor do saque maior que o saldo")
        else:
            print("Sem saldo disponivel para saque!")
            
           

    elif opcao == "e":
        print("************** EXTRATO **************")
        status = "Sem movimentações para exibir" if not extrato else extrato
        print(f"{status} \n")
        print(f"Seu Saldo Final: R$ {saldo:.2f}")
        print("************** FIM DO EXTRATO **************")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")