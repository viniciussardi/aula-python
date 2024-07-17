from banco import*

print("bem vindo ao caixa eletronico 2.0")


print("Menu inicial")
terminal = int(input("Escolha a operação que deseja fazer \n {1}Saque \n {2}Deposito \n {3}cadastrar um telefone \n {4}consultar saldo \n {5}Emprestimo "))
saldo_inicial = int(5000)
if terminal == 1:
    saque = int(input("Selecione o valor que deseja sacar: "))
    saldo_inicial = saque(saldo_inicial, saque)
    if saque <= saldo_inicial:
     print(f"voce acabou de sacar a {saque} seu saldo agora é de {saldo_inicial - saque}")
    elif saque > saldo_inicial:
         print("Seu saldo é insuficiente para sacar este valor!")
    else:
         print("Digite um valor valido!")
elif terminal == 2:
        deposito = int(input("Digite o valor que deseja depositar: "))
        saldo_inicial = deposito(saldo_inicial, deposito)
        print(f"seu saldo agora é de {saldo_inicial + deposito}")
  
