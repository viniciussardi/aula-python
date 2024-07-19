from sistema import*

print("Ola seja bem vindo ao sistema de empresa GUT!")

while True:
 menu = int(input("menu inicial: \n Selecione a opção que deseja executar: \n {1} Cadastrar usuario \n {2} Cadastrar contatos \n {3} Consultar ajuste de salario \n {4} Calculadora \n {5} Sair \n"))

 if menu == 1:
    nome_cad = nome1()
    endereco_cad = endereco1()
    setor_cad = setor1()
    cargo_cad = cargo1()
    print(f"Usuario cadastrado com sucesso! seja bem vindo a empresa! \nnome: {nome_cad} \nendereço: {endereco_cad} \nsetor: {setor_cad} \ncargo: {cargo_cad}")

 elif menu == 2:
    select = int(input("Selecione qual o tipo de contato que deseja cadastrar: \n {1} E-mail \n {2} Telefone \n {3} Celular \n"))
    if select == 1:
        e_cad = mail1()
        print(f"o e-mail {e_cad} foi cadastrado com sucesso!") 
    elif select == 2:
        tel_cad = tel1() 
        print(f"O telefone {tel_cad} foi cadastrado com sucesso!") 
    elif select == 3:
        cel_cad = cel1()
        print(f"O numero de celular {cel_cad} foi cadastrado com sucesso!")
    else:
        print("Digite um valor valido!")

 elif menu == 3:
    salario = float(input("Digite qual é o seu salario atual: "))
    if salario > 0 and salario <= 2000:
        calc1 = sal1(salario)
        print(f"Seu salario apos o dissidio sera: {calc1}")
    elif salario > 2000 and salario <= 3000:
        calc2 = sal2(salario)
        print(f"Seu salario apos o dissidio sera: {calc2}")
    elif salario > 3000:
        calc3 = sal3(salario)
        print(f"Seu salario apos o dissidio sera: {calc3}")
    elif salario < 0:
        print("Digite um salario maior que zero!")

 elif menu == 4:
    visor = int(input("elcolha qual operação deseja fazer na calculadora: \n {1}Soma \n {2}Subtração \n {3}Multiplicação \n {4}Divisão \n {5}porcentagem \n {6} exponenciação \n {7} tabuada \n"))
    if visor == 1:
        print("Digite dois dumeros para serem somados")
        first = float(input("1° numero: "))
        second = float(input("2° numero: "))
        soma = som1(first, second)
        print(f"O resultado da sua soma é: {soma}")
    elif visor == 2:
        print("Digite dois numeros, o segundo sera subtraido do primeiro. ")
        first2 = float(input("1° numero: "))
        second2 = float(input("2° numero: "))
        subt2 = sub1(first2, second2)
        print(f"O resultado da sua subtração é: {subt2}")
    elif visor == 3:
        print("Digite dois numeros que serão multiplicados um pelo outro. ")
        first3 = float(input("1° numero: "))
        second3 = float(input("2° numero: "))
        multi = mult1(first3, second3)
        print(f"O resultado da sua multiplicação é: {multi}")
    elif visor == 4:
        print("Digite dois numeros, o primeiro sera dividido pelo segundo. ")
        first4 = float(input("1° numero: "))
        second4 = float(input("2° numero: "))
        divis = div1(first4, second4)
        print(f"O resultado da sua divisão é: {divis}")
    elif visor == 5:
        print("Digite um numero e descubra qualquer porcentagem dele. ")
        first5 = float(input("Numero: "))
        second5 = float(input("Porcentagem: "))
        percent = per1(first5, second5)
        print(f"A porcentagem que você procura é: {percent}")
    elif visor == 6:
        print("Digite dois numeros, sera feita uma exponenciação deles ")
        first6 = float(input("1° numero: "))
        second6 = float(input("2° numero: "))
        exp = exp1(first6, second6)
        print(f"O resultado da sua exponenciação é: {exp}")
    elif visor == 7:
        print("Digite um numero e descubra a tabuada dele ")
        numeroT = float(input("numero: "))
        tabuada = tab1(numeroT)
        print(tabuada)
 elif menu == 5:
     print("Operação encerrada!")
     break
 else:
     print("Digite um valor valido!")
    