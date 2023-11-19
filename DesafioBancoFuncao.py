import textwrap


def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [c] Cadastrar Cliente
    [nc] Nova Conta
    [lc] Listar Contas


    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t + R$ {valor:.2f}\n"

    else:
        print(f"Deposito no Valor de R$:{valor:.2f} Realizado com sucesso!")
        print(f"\nSeu novo saldo é de R$:{saldo:.2f} Realizado com sucesso!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques ):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t\t\t- R$ {valor:.2f} \n"
        numero_saques += 1
        print(f"Saque no Valor de R$:{valor:.2f} Realizado com sucesso!")

    else:
        print("!!! Operação falhou! Refaça a operação !!!")
    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    if saldo>=0:
        print(f"\nSaldo: R$ {saldo:.2f}") 
    else: 
        print(f"\n Saldo: - R$ {saldo:.2f}")
    
    print("==========================================")
    

def cadastrar_cliente(clientes):
    cpf = float(input("Informe o seu CPF (!SOMENTE NUMEROS!): "))
    if verifica_cliente(clientes,cpf):
        print("Cliente ja cadastrado com este cpf")
    else:
        nome_completo = input("Informe seu nome sobre nome completos: ")
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaa): ")
        endereço = input("Qual o seu endereço (Logradouro - Numero - Bairro - Cidade/Estado(Sigla)): ")
        clientes.append({"nome": nome_completo,"data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereço})
        
            
    
def verifica_cliente(clientes, cpf):
    resultado = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return resultado[0] if resultado else None


def nova_conta(agencia, clientes, numero_conta, contas):
    cpf = float(input("Informe o seu CPF (!SOMENTE NUMEROS!): "))
    cliente  = verifica_cliente(clientes,cpf)
    if cliente:        
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente})
        print("Conta Criada com sucesso!")

    else:
        print("Cliente não cadastrado!!! \n Cadastre um novo cliente antes de criar uma nova conta! ")

def listar_contas(Contas):
    for conta in contas:
        print(f"Agencia: {conta['agencia']}\n Numero:{conta['numero_conta']}\n Cliente:{conta['cliente']['nome']}\n  ")









saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
clientes = []
contas = []


while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo = saldo, valor = valor, extrato= extrato, limite = limite, numero_saques = numero_saques, limite_saques=LIMITE_SAQUES )

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        cadastrar_cliente(clientes)

    elif opcao == "nc":
        numero_conta = len(contas)+1
        nova_conta(AGENCIA, clientes, numero_conta, contas  )

    elif opcao == "lc":
        listar_contas(contas)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")











