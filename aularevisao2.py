nome = (input("Digite o nome do seu produto: "))
empresa = input("Digite o nome da sua empresa: ")
ean13_codigoDeBarras = input("Digite o codigo de barras do seu produto: ")
sabor = input("Digite o sabor do produto: ")
Kcal = float(input("Digite quantas calorias seu produto possui: "))
volume = float(input("Digite quantos litos/ml tem seu produto: "))
desing = input("Descreva o desing da sua embalagem: ")
fabricação = input("Digite os dados da fabricação do seu produto: ")
validade = input("Digite a validade do seu produto: ")
receita = input("Digite a receita do seu produto: ")
armazenamento = input("descreva o armazenamento adequado para seu produto: ")
embalagem = input("Descreva a embalagem do seu produto: ")
preco = float(input("digite o preco do seu produto: "))


print(("nome:") + nome )
print(("empresa:") + empresa)
print(("codigo de barras") + ean13_codigoDeBarras)
print(("sabor:") + sabor)
print(("quantidade de calorias:") + Kcal)
print(("volume do produto:") + volume)
print(("Desing do produto:") + desing)
print(("Dados da fabricação") + fabricação)
print(("Validade:") + validade)
print(("ingredientes do produto") + receita)
print(("Descrição do armazenamento") + armazenamento)