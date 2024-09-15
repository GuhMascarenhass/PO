import numpy as np
"""
Esse codigo foi inteiramente feito pelo CHAT GPT.
É apenas um script de estudo e para ter uma noção de como implementar
"""

def simplex(c, A, b):
    """
    Resolve o problema de programação linear usando o método Simplex.

    Minimize c^T * x
    Sujeito a A * x <= b
    x >= 0
    """
    #Inverte os sinais dos coeficientes da função objetivo para minimizar
    #c = -c

    m, n = A.shape

    # Adiciona variáveis de folga
    A = np.hstack([A, np.eye(m)])
    c = np.hstack([c, np.zeros(m)])

    # Tabela Simplex inicial
    tableau = np.vstack([np.hstack([A, b.reshape(-1, 1)]), np.hstack([-c, [0]])])

    while np.any(tableau[-1, :-1] < 0):
        # Seleciona a coluna pivô
        pivot_col = np.argmin(tableau[-1, :-1])

        # Seleciona a linha pivô
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        pivot_row = np.where(ratios > 0, ratios, np.inf).argmin()

        # Atualiza a tabela
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for r in range(tableau.shape[0]):
            if r != pivot_row:
                tableau[r, :] -= tableau[r, pivot_col] * tableau[pivot_row, :]

    return tableau[-1, -1], tableau[:-1, -1]


def main():
    print("Programa Simplex para Programação Linear")

    # Solicita ao usuário o número de variáveis e restrições
    num_vars = int(input("Número de variáveis de decisão: "))
    num_constraints = int(input("Número de restrições: "))

    # Solicita ao usuário os coeficientes da função objetivo
    print("Digite os coeficientes da função objetivo (separados por espaço):")
    c = np.array([float(x) for x in input().split()])

    if len(c) != num_vars:
        raise ValueError(
            "O número de coeficientes da função objetivo deve corresponder ao número de variáveis de decisão.")

    # Solicita ao usuário os coeficientes das restrições
    A = np.zeros((num_constraints, num_vars))
    b = np.zeros(num_constraints)
    

    for i in range(num_constraints):
        print(f"Digite os coeficientes da restrição {i + 1} (separados por espaço):")
        A[i] = np.array([float(x) for x in input().split()])
        print(f"Digite o valor final da restrição {i + 1}:")
        b[i] = float(input())

    if A.shape[1] != num_vars:
        raise ValueError("O número de coeficientes das restrições deve corresponder ao número de variáveis de decisão.")

    # Resolve o problema usando o método Simplex
    optimal_value, solution = simplex(c, A, b)

    print("Valor ótimo:", optimal_value)
    print("Solução ótima:", solution)


if __name__ == "__main__":
    main()


