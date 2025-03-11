def eliminacao_de_gauss(A, b):
    """
    Resolve um sistema linear Ax = b usando o método de Eliminação de Gauss e imprime os passos detalhados.

    Parâmetros:
    A (list of lists): Matriz dos coeficientes.
    b (list): Vetor de termos independentes.

    Retorna:
    list: Solução do sistema linear.
    """
    n = len(A)  # Número de linhas (ou colunas) da matriz

    print("=== Método de Eliminação de Gauss ===")
    print("Matriz A (coeficientes do sistema):")
    for row in A:
        print(row)
    print(f"\nVetor b (termos independentes): {b}\n")

    # Eliminação para obter uma matriz triangular superior
    for k in range(n):
        print(f"Passo {k+1}: Eliminando variáveis na coluna {k}")
        # Pivô parcial: troca de linhas para colocar o maior elemento na diagonal principal
        max_index = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[max_index][k] == 0:
            raise ValueError("Sistema sem solução ou infinitas soluções (linha com zero na diagonal principal)")

        # Troca de linhas se necessário
        if max_index != k:
            A[k], A[max_index] = A[max_index], A[k]
            b[k], b[max_index] = b[max_index], b[k]
            print(f"  - Trocando linha {k} com linha {max_index} para pivô parcial")

        print(f"  - Matriz A após troca de linhas (se aplicável):")
        for row in A:
            print("   ", row)
        print(f"  - Vetor b após troca de linhas (se aplicável): {b}\n")

        # Eliminação de Gauss
        for i in range(k+1, n):
            fator = A[i][k] / A[k][k]
            print(f"  - Eliminando A[{i}][{k}] usando fator: {fator}")
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
            b[i] -= fator * b[k]
            print(f"    - Linha {i} após eliminação: {A[i]} | b[{i}] = {b[i]}\n")

    print("=== Matriz Triangular Superior ===")
    for row in A:
        print(row)
    print(f"Vetor b após eliminação: {b}\n")

    # Resolução por substituição retroativa (sistema triangular superior)
    x = [0] * n
    print(">>> Iniciando a Substituição Retroativa <<<\n")
    for i in range(n-1, -1, -1):
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
    [2, -1, 6],   # Coeficientes da primeira equação: 2x0 - x1 + x2 = 5
    [4, -2, 1],    # Coeficientes da segunda equação: x0 + 2x2 = 6
    [1, -5, -2]    # Coeficientes da terceira equação: 3x0 + 2x1 - x2 = 4
]
b = [3, 2, -4]  # Termos independentes correspondentes às equações acima

# Chamando a função para resolver o sistema e imprimir os passos
solucao = eliminacao_de_gauss(A, b)