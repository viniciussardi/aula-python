vel = 50

opcao = input(f"Sua velocidade inicial é{vel}. Você deseja aumentear oudiminuir a velocidade?")

if opcao == "a" :
    vel = vel + 10 
    print(f"Sua velocidade atual é {vel}")

elif opcao == "b":
    vel = vel -10
    print(f"Sua velocidade atual é {vel}")

else:
    print("exiba um valor valido")