def teste_simplex():
    # Função objetivo: Max Z = 4x1 + 3x2
    obj = [4, 3]  # Coeficientes da função objetivo
    
    # Restrições:
    # 2x1 + x2 <= 8  (representado como [2, 1, 8])
    # x1 + 2x2 <= 6  (representado como [1, 2, 6])
    decision = [
        [2, 1, 8],   # Primeira restrição
        [1, 2, 6]    # Segunda restrição
    ]
    
    # Número de variáveis de decisão e restrições
    d = 2  # Número de variáveis de decisão (x1, x2)
    r = 2  # Número de restrições

    # Montar o tableau inicial
    tableau = montar_tableau(obj, decision, d, r)

    # Resolver usando o método Simplex
    simplex(tableau)

# Chamar a função de teste

def choice_min_max():
    escolha = int(input("1 para Max, 2 para Min: "))
    return escolha

def size_simplex():
    d = int(input("Número de variáveis de decisão: "))
    r = int(input("Número de restrições: "))
    return d, r

def montar_tableau(obj, decision, d, r):
    # Criando o tableau (adicionando as variáveis de folga)
    tableau = []

    # Adicionar as restrições ao tableau, com variáveis de folga
    for i in range(r):
        row = decision[i][:d] + [0]*r + [decision[i][-1]]
        row[d + i] = 1  # Adicionar 1 para a variável de folga
        tableau.append(row)

    # Adicionar a função objetivo (negativa para maximização)
    obj_row = [-val for val in obj] + [0] * (r + 1)  # Variáveis de folga e a coluna de solução
    tableau.append(obj_row)

    return tableau

def print_tableau(tableau):
    print("\nTableau atual:")
    for row in tableau:
        print("\t".join([f"{v:.2f}" for v in row]))

def encontrar_coluna_pivo(tableau):
    # Encontrar a coluna de pivô (variável que entra na base)
    obj_row = tableau[-1]
    col_pivo = min(range(len(obj_row) - 1), key=lambda c: obj_row[c])  # Exclui o valor na coluna de solução
    if obj_row[col_pivo] >= 0:
        return -1  # Já está otimizado (maximização)
    return col_pivo

def encontrar_linha_pivo(tableau, col_pivo):
    # Encontrar a linha de pivô (variável que sai da base)
    linhas_pivo = []
    for i in range(len(tableau) - 1):  # Exceto a linha da função objetivo
        if tableau[i][col_pivo] > 0:  # Apenas consideramos coeficientes positivos na coluna pivô
            razao = tableau[i][-1] / tableau[i][col_pivo]
            linhas_pivo.append((razao, i))  # Guardamos a razão e o índice da linha

    if not linhas_pivo:
        return -1  # Sem solução ótima (não há valores positivos na coluna pivô)

    # Escolher a linha com a menor razão
    _, linha_pivo = min(linhas_pivo)
    return linha_pivo

def realizar_pivo(tableau, linha_pivo, col_pivo):
    # Dividir a linha pivô pelo valor na posição de pivô
    pivo = tableau[linha_pivo][col_pivo]
    tableau[linha_pivo] = [val / pivo for val in tableau[linha_pivo]]

    # Zerar os outros valores da coluna pivô
    for i in range(len(tableau)):
        if i != linha_pivo:
            fator = tableau[i][col_pivo]
            tableau[i] = [tableau[i][j] - fator * tableau[linha_pivo][j] for j in range(len(tableau[i]))]

def simplex(tableau):
    while True:
        print_tableau(tableau)

        # 1. Encontrar a coluna do pivô (variável que entra)
        col_pivo = encontrar_coluna_pivo(tableau)
        if col_pivo == -1:
            print("Solução ótima encontrada!")
            break

        # 2. Encontrar a linha do pivô (variável que sai)
        linha_pivo = encontrar_linha_pivo(tableau, col_pivo)
        if linha_pivo == -1:
            print("Problema sem solução ótima.")
            break

        # 3. Realizar o pivô
        realizar_pivo(tableau, linha_pivo, col_pivo)

    print("\nSolução ótima:")
    for i in range(len(tableau) - 1):
        print(f"x{i+1} = {tableau[i][-1]:.2f}")
    print(f"Valor da função objetivo: {tableau[-1][-1]:.2f}")



# Coleta de dados
decision = []
obj = []
d, r = size_simplex()

# Coleta da função objetivo
if choice_min_max() == 1:
    for y in range(d):
        obj.append(int(input(f"Coeficiente da variável x{y+1} na função objetivo: ")))

    # Coleta das restrições
    for y in range(r):
        decision.append([])
        for x in range(d + 1):
            if x == d:
                decision[y].append(int(input(f"Valor final da restrição {y+1}: ")))
            else:
                decision[y].append(int(input(f"Coeficiente da variável x{x+1} na restrição {y+1}: ")))

# Montar o tableau inicial
tableau = montar_tableau(obj, decision, d, r)
teste_simplex()
print("=-"*20)

# Resolver usando o método Simplex

simplex(tableau)
