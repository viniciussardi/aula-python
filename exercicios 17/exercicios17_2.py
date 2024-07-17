import time

print("Bora fazer um Bolo!!!")
print("Veja seus ingredientes você irá precisar de 3 ovos, 2 xicaras de açucar, 3 xicaras de trigo, 2 colheres de "
      "manteiga, 2 xicaras de leite e 2 colheres de fermento")
time.sleep(2)
ovos = 3
xAcucar = 2
xTrigo = 3
cManteiga = 2
xLeite = 2
cFermento = 1
print("Pré-aqueça o forno em 256°")
time.sleep(2)
print("Untar a forma com manteiga e farinha")
time.sleep(2)
print("Bora pegar os ingredientes")
time.sleep(3)
# Laço de repetição:

# for - utilizo quando sei quantas vezes eu vou usar ou executar uma ação.
# while - uso até que uma condição seja feita.
# Laço de repetição de quebrar os ovos

for cont in range(1, ovos+1):
    print(f"Quebre o ovo {cont}°, coloque o conteudo na tigela, jogue a casca no lixo")
    time.sleep(3)
for cont in range(1, xAcucar+1):
    print("Pegue o Açucar, e coloque na xicara até sua borda, reserve o açucar, e coloque na tijela")
    time.sleep(3)
for cont in range(1, xTrigo+1):
    print("Pegue o Trigo, coloque na xicara até sua borda, reserve a farinha, e coloque na tijela")
    time.sleep(3)
for cont in range(1, cManteiga+1):
    print("Pegue uma colher e pegue a quantidade de manteiga correspondente, e coloque na tijela")
    time.sleep(3)
for cont in range(1, xLeite+1):
    print(f"Pegue 250ml de leite e coloque a xicara{cont}° na tijela")
    time.sleep(3)
for cont in range(1, cFermento+1):
    print(f"pegue uma colher de fermento e coloque na tijela")
    time.sleep(3)
print("Misture todos os ingredientes")
print("Coloque no forno")
print("Espere 40 minutos")
time.sleep(40)