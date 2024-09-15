def choice_min_max():
    # Metodo para escolha de minimização ou maximização
    choice = int(input("1 para Max, 2 para Min: "))
    return choice


def size_simplex():
    # Função para definir as dimensoes do problema
    d = int(input("Número de variáveis de decisão: "))
    r = int(input("Número de restrições: "))
    return d, r


def tableau(obj, decision, d, r):
    tableau = []
    # Fazer o tableau com as variaveis de folga
    for i in range(r):
        row = decision[i][:d] + [0]*r + [decision[i][-1]]
        # qual é a respectiva variavel de folga
        row[d + i] = 1  
        tableau.append(row)

    obj_row = obj + [0] * (r + 1)  # Variáveis de folga e a coluna de solução
    tableau.append(obj_row)

    return tableau


def print_tableau(tableau):
    print("\nTableau atual:")
    for row in tableau:
        print("\t".join([f"{v:.2f}" for v in row]))


def pivo_colunm(tableau):
    # Encontrar a coluna de pivô (variável que entra na base)
    obj_row = tableau[-1]
    col_pivo = min(range(len(obj_row) - 1), key=lambda c: obj_row[c])  # Exclui o valor na coluna de solução
    if obj_row[col_pivo] >= 0:
        return -1  
    return col_pivo


def pivo_row(tableau, col_pivo):
    # Encontrar a linha de pivô (variável que sai da base)
    rows_pivo = []
    for i in range(len(tableau) - 1):  # Exceto a linha da função objetivo
        if tableau[i][col_pivo] > 0:  # Apenas consideramos coeficientes positivos na coluna pivô
            c = tableau[i][-1] / tableau[i][col_pivo]
            rows_pivo.append((c, i))  # Guardamos a razão e o índice da linha

    if not rows_pivo:
        return -1  
    _, row_pivo = min(rows_pivo)
    return row_pivo


def make_pivo(tableau, row_pivo, col_pivo):
    # Dividir a linha pivô pelo valor na posição de pivô
    pivo = tableau[row_pivo][col_pivo]
    tableau[row_pivo] = [val / pivo for val in tableau[row_pivo]]

    # Zerar os outros valores da coluna pivô
    for i in range(len(tableau)):
        if i != row_pivo:
            fator = tableau[i][col_pivo]
            tableau[i] = [tableau[i][j] - fator * tableau[row_pivo][j] for j in range(len(tableau[i]))]


def simplex(tableau):
    while True:
        print_tableau(tableau)

        # 1. Encontrar a coluna do pivô (variável que entra)
        col_pivo =pivo_colunm(tableau)
        if col_pivo == -1:
            print("Solução ótima encontrada!")
            break

        # 2. Encontrar a linha do pivô (variável que sai)
        linha_pivo = pivo_row(tableau, col_pivo)
        if linha_pivo == -1:
            print("Problema sem solução ótima.")
            break

        # 3. Realizar o pivô
        make_pivo(tableau, linha_pivo, col_pivo)

    print("\nSolução ótima:")
    for i in range(len(tableau) - 1):
        print(f"x{i+1} = {tableau[i][-1]:.2f}")
    print(f"Valor da função objetivo: {tableau[-1][-1]:.2f}")


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
tableau = tableau(obj, decision, d, r)
print("=-"*20)

# Resolver usando o método Simplex

simplex(tableau)
