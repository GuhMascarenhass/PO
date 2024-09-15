header = []
header_number = [] 
max_min = int(input("é um problema de Maximização ou Minimização: (1 ou 0) "))
i = int(input("Quantas icnonitas "))
if max_min == 1:
   for x in range(0, i): 
        header.append(input("Icnonita:"))
    if int(input("deseja adiconar mais um? (1 S / 0 N) ")) == 0:
        header_number.append(int("Apenas o coeficiênte "))
    if int(input("deseja adiconar mais um? (1 S / 0 N) ")) == 0:
        break

    elif max_min == 0:

for i in range(0, len(funcao_objetiva)):
    for j in funcao_objetiva[i]:
        x = funcao_objetiva[i]
