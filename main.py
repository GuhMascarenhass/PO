import numpy as np
variaveis_list = []
restricoes_list = []
max_funcao = input("Escreva a função objetiva")
for cont in range(0, 10):
    variaveis_list.append(float(input("Digite a variável: ")))
    if input("Deseja continuar? (0 sair)") == "0":
        break
