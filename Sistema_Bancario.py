saque = 1500
saldo = 0
deposito = 0
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    print("""
    ============ Menu ============          
    =       1 - Depositar        =
    =       2 - Sacar            =
    =       3 - Extrato          =
    =       4 - Sair             =
    ==============================

    """)
    menu = int(input("Qual operação deseja realizar?"))

    ### Bloco Desposito ###
    if menu == 1:

        deposito  = float(input("Qual o valor do deposito: "))

        if deposito >= 1 :
            saldo += deposito   
            print("Deposito efetuado com sucesso! \n") 
            print(f"Seu saldo é de: {saldo} \n")
            extrato += f"Depósito : R$ {deposito:.2f}\n"
        else:
                print("Não é possivel deposito de valores negativo  ")        

        
    ### Bloco Saque ###
    elif menu == 2:

        if saldo != 0:
            print("Vc escolheu Saque: ")
            print(f"Saldo atual {saldo}")
            saque = float(input("Qual o valor do saque: "))
            if numero_saque < LIMITE_SAQUES:
                if saque <= 500:
                    if saldo >= saque:
                        saldo -= saque
                        print("Operação realizada com sucesso!")
                        extrato += f"Saque : R$ {saque:.2f}\n"
                        numero_saque += 1
                    else:
                        print(f"saldo insuficiente! SALDO ATUAL: {saldo} \n")              
                else:
                    print("Operação não realizada, valor maximo para saque R$ 500")
            else:
                print("Oeração não realizada, Número máximo de saques excedido.")


    ### Bloco Extrato ###        
    elif menu == 3:

        print("\n############ EXTRATO ############")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    else:

        menu == 4
        print("Vc escolheu Sair")
        break
