import numpy as np
from scipy.linalg import lu

def verificar_matriz_quadrada(A):
    """
    Verifica se a matriz A é quadrada.

    :param A: matriz numpy
    :return: True se for quadrada, False caso contrário
    """
    return A.shape[0] == A.shape[1]

def verificar_fatoracao_LU(A):
    """
    Verifica se a matriz A pode ser fatorada como LU sem pivotamento.

    :param A: matriz numpy
    :return: True se for possível a fatoração LU sem pivotamento, False caso contrário
    """
    n = A.shape[0]

    for i in range(n):
        sub_matriz = A[:i+1, :i+1]  # Menor principal de ordem i+1
        if np.linalg.det(sub_matriz) == 0:
            return False

    return True

def fatoracao_LU(A):
    """
    Tenta realizar a fatoração LU da matriz A.

    :param A: matriz numpy
    :return: matrizes L e U se a fatoração for possível, caso contrário None
    """
    if not verificar_matriz_quadrada(A):
        print("A matriz não é quadrada e, portanto, não pode ser fatorada por LU.")
        return None

    if not verificar_fatoracao_LU(A):
        print("A matriz não satisfaz os critérios para a fatoração LU sem pivotamento.")
        return None

    P, L, U = lu(A)  # Fatoração LU com pivotamento (Scipy inclui o pivotamento)
    return L, U

def main():
    # Entrada da matriz pelo usuário
    ordem = int(input("Digite a ordem da matriz (número de linhas/colunas): "))

    print("Digite os elementos da matriz linha por linha:")
    A = []
    for i in range(ordem):
        linha = list(map(float, input(f"Digite os elementos da linha {i+1} separados por espaço: ").split()))
        A.append(linha)

    A = np.array(A)

    # Tenta realizar a fatoração LU
    resultado = fatoracao_LU(A)

    if resultado is not None:
        L, U = resultado
        print("\nA matriz pode ser fatorada por LU.")
        print("Matriz L (inferior):")
        print(L)
        print("Matriz U (superior):")
        print(U)
    else:
        print("Não é possível realizar a fatoração LU na matriz fornecida.")

if __name__ == "__main__":
    main()