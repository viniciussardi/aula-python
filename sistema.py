def nome1():
  nome = (input("Digite o nome do usuario que sera cadastrado: "))
  return nome

def endereco1():
    endereco = input("Digite o endereço do usuario: ")
    return endereco

def setor1():
    setor = input("Digite o setor do usuario: ")
    return setor

def cargo1():
    cargo = input("Digite o cargo do usuario: ")
    return cargo

def mail1():
    email = input("Digite o e-mail que vai ser cadastrado: ")
    return email

def tel1():
    tel = input("Digite o telefone a ser cadastrado: ")
    return tel

def cel1():
    cel = input("Digite o numero de celular a ser cadastrado")
    return cel

def sal1(salario):
    calc = salario * 0.2
    return salario + calc 

def sal2(salario):
    cal = salario * 0.13
    return salario + cal

def sal3(salario):
    cal1 = salario * 0.07
    return salario + cal1

def som1(first, second):
    som2 = first + second
    return som2

def sub1(first2, second2):
    sub = first2 - second2
    return sub

def mult1(first3, second3):
    multip = first3 * second3
    return multip

def div1(first4, second4):
    divisão = first4 / second4
    return divisão

def per1(first5, second5):
    porcent = first5 / 100
    return porcent * second5

def exp1(first6, second6):
    exppo = first6 ** second6
    return exppo


def tab1(numeroT):
    contador = 1
    for contador in range(1,11):
      tab = contador * numeroT
      return tab
