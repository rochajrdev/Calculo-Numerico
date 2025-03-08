def resolver_sistema_triangulo_inferior(A, b):
    """
    Resolve um sistema linear triangular inferior Ax = b e imprime os passos detalhados.

    Parâmetros:
    A (list of lists): Matriz triangular inferior.
    b (list): Vetor de termos independentes.

    Retorna:
    list: Solução do sistema linear.
    """
    n = len(b)  # Número de equações no sistema
    x = [0] * n  # Inicializa o vetor solução com zeros

    print("=== Resolução do Sistema Triangular Inferior ===")
    print(f"Matriz A (coeficientes do sistema):")
    for row in A:
        print(row)
    print(f"\nVetor b (termos independentes): {b}\n")
    print(">>> Iniciando a Substituição Progressiva <<<\n")

    # Resolução por substituição progressiva
    for i in range(n):
        print(f"Passo {i+1}: Resolvendo para a variável x[{i}]")

        # Inicializa a soma dos produtos dos coeficientes com as soluções já conhecidas
        soma = 0
        for j in range(i):
            produto = A[i][j] * x[j]
            soma += produto
            print(f"  - Multiplicando coeficiente A[{i}][{j}] = {A[i][j]} pelo valor da variável x[{j}] = {x[j]} -> Produto = {produto}")

        # Calcula o valor da variável x[i] usando a fórmula: (b[i] - soma) / A[i][i]
        x[i] = (b[i] - soma) / A[i][i]
        print(f"  - Soma dos produtos das variáveis já calculadas: {soma}")
        print(f"  - Calculando x[{i}] usando: (termo independente b[{i}] = {b[i]} - soma) / coeficiente A[{i}][{i}] = {A[i][i]}")
        print(f"  - x[{i}] = ({b[i]} - {soma}) / {A[i][i]} = {x[i]}\n")

    print("=== Solução Completa do Sistema ===")
    print(f"Vetor solução x: {x}")
    return x

# Exemplo de uso:
A = [
    [2, 0, 0],  # Coeficiente da primeira equação: 2x0 = 4
    [1, 3, 0],  # Coeficientes da segunda equação: x0 + 3x1 = 6
    [4, -1, 1]  # Coeficientes da terceira equação: 4x0 - x1 + x2 = 5
]
b = [4, 6, 5]  # Termos independentes correspondentes às equações acima

# Chamando a função para resolver o sistema e imprimir os passos
solucao = resolver_sistema_triangulo_inferior(A, b)
