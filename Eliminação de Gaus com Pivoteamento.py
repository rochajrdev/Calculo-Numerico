def eliminacao_de_gauss_com_pivoteamento(A, b):
    """
    Resolve um sistema linear Ax = b usando o método de Eliminação de Gauss com pivoteamento parcial,
    mostrando todos os passos, escolhas de pivô, trocas de linhas e a nova matriz em cada etapa.

    Parâmetros:
    A (list of lists): Matriz dos coeficientes.
    b (list): Vetor de termos independentes.

    Retorna:
    list: Solução do sistema linear.
    """
    n = len(A)  # Número de equações (linhas da matriz)

    print("=== Método de Eliminação de Gauss com Pivoteamento Parcial ===")
    print("Matriz A (coeficientes do sistema):")
    for row in A:
        print(row)
    print(f"\nVetor b (termos independentes): {b}\n")

    # Fase de Eliminação para transformar A em uma matriz triangular superior
    for k in range(n):
        print(f"Passo {k+1}: Trabalhando com a coluna {k}")

        # Pivô parcial: escolher o maior elemento da coluna k para o pivô
        max_index = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[max_index][k] == 0:
            raise ValueError("Sistema sem solução única (zero encontrado na diagonal principal)")

        # Troca de linhas para garantir o maior pivô
        if max_index != k:
            A[k], A[max_index] = A[max_index], A[k]
            b[k], b[max_index] = b[max_index], b[k]
            print(f"  - Trocando linha {k} com linha {max_index} para maximizar o pivô")
            print(f"  - Nova Matriz A após troca de linhas:")
            for row in A:
                print("   ", row)
            print(f"  - Vetor b após troca: {b}\n")

        # O elemento pivô é A[k][k]
        pivô = A[k][k]
        print(f"  - Pivô escolhido: A[{k}][{k}] = {pivô}\n")

        # Eliminação para zerar os elementos abaixo do pivô
        for i in range(k+1, n):
            fator = A[i][k] / pivô
            print(f"  - Eliminando elemento A[{i}][{k}] com fator: {fator}")
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
                print(f"    - Atualizando A[{i}][{j}]: {A[i][j]}")
            b[i] -= fator * b[k]
            print(f"  - Nova linha {i} de A: {A[i]} | Novo b[{i}] = {b[i]}\n")

    print("=== Matriz Triangular Superior ===")
    for row in A:
        print(row)
    print(f"Vetor b após eliminação: {b}\n")

    # Fase de Substituição Retroativa para resolver o sistema triangular superior
    x = [0] * n
    print(">>> Iniciando a Substituição Retroativa <<<\n")
    for i in range(n-1, -1, -1):
        # Soma dos produtos dos coeficientes com as soluções já calculadas
        soma = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - soma) / A[i][i]
        print(f"Passo {n-i}: Resolvendo para x[{i}]")
        print(f"  - Soma dos produtos das variáveis já calculadas: {soma}")
        print(f"  - Calculando x[{i}] usando: (termo independente b[{i}] = {b[i]} - soma) / coeficiente A[{i}][{i}] = {A[i][i]}")
        print(f"  - x[{i}] = ({b[i]} - {soma}) / {A[i][i]} = {x[i]}\n")

    print("=== Solução Completa do Sistema ===")
    print(f"Vetor solução x: {x}")
    return x

# Exemplo de uso:
A = [
    [2, -1, 1],   # Coeficientes da primeira equação: 2x0 - x1 + x2 = 5
    [1, 0, 2],    # Coeficientes da segunda equação: x0 + 2x2 = 6
    [3, 2, -1]    # Coeficientes da terceira equação: 3x0 + 2x1 - x2 = 4
]
b = [5, 6, 4]  # Termos independentes correspondentes às equações acima

# Chamando a função para resolver o sistema e imprimir os passos
solucao = eliminacao_de_gauss_com_pivoteamento(A, b)
