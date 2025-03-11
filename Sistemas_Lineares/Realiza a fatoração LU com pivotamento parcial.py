import numpy as np
from scipy.linalg import lu

def fatoracao_lu(A):
    """
    Função que realiza a fatoração LU da matriz A.

    :param A: matriz quadrada do sistema linear
    :return: matrizes L e U da fatoração LU
    """
    P, L, U = lu(A)  # Realiza a fatoração LU com pivotamento parcial
    return L, U, P

def resolver_sistema_lu(L, U, P, b):
    """
    Função que resolve o sistema linear usando as matrizes L e U da fatoração LU.

    :param L: matriz triangular inferior da fatoração LU
    :param U: matriz triangular superior da fatoração LU
    :param P: matriz de permutação da fatoração LU
    :param b: vetor de termos independentes
    :return: solução do sistema linear
    """
    Pb = np.dot(P, b)  # Aplica a permutação no vetor b
    y = np.linalg.solve(L, Pb)  # Resolve Ly = Pb (substituição direta)
    x = np.linalg.solve(U, y)  # Resolve Ux = y (substituição retroativa)
    return x

def calcular_determinante(U):
    """
    Função que calcula o determinante da matriz original a partir da matriz U.

    :param U: matriz triangular superior da fatoração LU
    :return: determinante da matriz
    """
    det = np.prod(np.diag(U))  # O determinante é o produto dos elementos da diagonal de U
    return det

def main():
    # Solicita ao usuário a matriz aumentada
    n = int(input("Digite o número de equações (e variáveis): "))
    A = []
    b = []

    print("Digite os coeficientes das equações:")
    for i in range(n):
        linha = list(map(float, input(f"Coeficientes da equação {i+1}: ").split()))
        A.append(linha[:-1])
        b.append(linha[-1])

    A = np.array(A)
    b = np.array(b)

    try:
        # Realiza a fatoração LU
        L, U, P = fatoracao_lu(A)

        # Exibe as matrizes L, U e P
        print("\nMatriz L (Triangular Inferior):\n", L)
        print("\nMatriz U (Triangular Superior):\n", U)
        print("\nMatriz de Permutação P:\n", P)

        # Calcula o determinante da matriz
        det = calcular_determinante(U)
        print("\nDeterminante da matriz:", det)

        # Verifica se o sistema pode ser resolvido
        if det == 0:
            print("O sistema não pode ser resolvido pela fatoração LU (determinante zero).")
        else:
            # Resolve o sistema
            x = resolver_sistema_lu(L, U, P, b)
            print("\nSolução do sistema:\n", x)

    except Exception as e:
        print("Erro ao resolver o sistema:", str(e))

if __name__ == "__main__":
    main()
