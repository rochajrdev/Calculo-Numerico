import numpy as np

def verificar_fatoracao_lu(A):
    """
    Verifica se a matriz A pode ser fatorada em LU sem pivotamento,
    calcula o determinante e mostra o passo a passo da decomposição.

    :param A: matriz quadrada de coeficientes do sistema linear
    :return: True se for possível, False caso contrário
    """
    n = A.shape[0]
    L = np.eye(n)  # Inicializa L como uma matriz identidade
    U = A.copy()   # Copia A para começar a decomposição em U
    det = 1        # Inicializa o determinante

    print("Matriz inicial:")
    print(A)
    print()

    # Tentativa de fatoração LU sem pivotamento
    for i in range(n):
        # Checa se o pivô (diagonal principal) é zero
        if U[i, i] == 0:
            print(f"Pivô nulo encontrado na linha {i+1}, fatoração LU sem pivotamento não é possível.")
            return False

        # Atualiza o determinante multiplicando pelos pivôs
        det *= U[i, i]

        # Atualização dos elementos da matriz para a fatoração
        for j in range(i+1, n):
            fator = U[j, i] / U[i, i]  # Calcula o fator de eliminação
            U[j, i+1:] -= fator * U[i, i+1:]  # Atualiza a linha de U
            U[j, i] = 0  # Coloca zero abaixo do pivô na matriz U
            L[j, i] = fator  # Preenche o fator na matriz L

        # Mostra a matriz L e U a cada passo
        print(f"Passo {i+1}:")
        print("Matriz L:")
        print(L)
        print("Matriz U:")
        print(U)
        print()

    print(f"Determinante da matriz A: {det}")
    print("Fatoração LU concluída com sucesso.")
    return True

# Exemplo de uso:
A = np.array([
    [2, 3, -1],
    [4, 4, -3],
    [2, -3, 1]
], dtype=float)

# Chama a função para verificar a fatoração LU
possivel = verificar_fatoracao_lu(A.copy())

if possivel:
    print("Sistema pode ser resolvido usando LU sem pivotamento.")
else:
    print("Necessário pivotamento para resolver o sistema usando LU.")

    '''Sim, é possível resolver o sistema linear pelo método de fatoração LU sem pivotamento. O determinante da matriz é
−
20
−20, indicando que a matriz é não singular. A fatoração LU foi realizada com sucesso, mostrando que todos os pivôs foram não nulos.'''
