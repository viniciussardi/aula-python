
senha = 456739
saldo = 3000

produto = input("Bem vindo a loja! Digite o produto que deseja comprar: ")
preco = float(input("Qual o preço do produto: "))

formpgmt = int(input("Forma de pagamento \n {1}-Dinheiro\n {2}-Credito\n {3}-Debito\n {4}-Pix"))


if formpgmt == 1:
    din = float(input("Qual o valor dado em especie? "))
    if (din > preco):
        print("obrigado pela compra, Seu troco é de:", din - preco)
    elif(din == preco):
        print("obrigado pela compra, volte sempre")
    else:
        print("O valor dado não é suficiente para a compra! ")
elif formpgmt == 2:
    limite = float(input("qual seu limite?"))
    if (limite >= preco):
        op = input("Deseja parcelar sua compra? S - sim ou N - nao ")
        if(op == 'N'):
            transacao = int(input("Digite sua senha"))
            if transacao == senha:
              print("Obrigado por comprar com a gente! Volte sempre.")
            else:
                print("Senha incorreta")
        elif(op == 'S'):
            nparcela = int(input("Em quantas parcelas? O valor deve ser maior do que 0"))
            transacao = int(input("Digite sua senha"))
            if transacao == senha:
             print("Obrigado por comprar com a gente! sua parcela e de: ", preco/nparcela)
            else:
                print("Senha incorreta!")
        else:
            print("Digite um valor valido!")
    else:
        print("Obrigado por comprar com a gente! Volte sempre.")
elif formpgmt == 3:
    transacao = int(input("Digite sua senha"))
    print(transacao, senha)
    if transacao == senha:
        if saldo < preco:
         print("Saldo insufuciente!")
        else:
           print("Obrigado por comprar com a gente! Volte sempre.")
    else:
        print("Senha incorreta!")
elif formpgmt == 4:
    print("Obrigado por comprar com a gente! Volte sempre.")
else:
    print("Digite um valor valido!")


    
    



