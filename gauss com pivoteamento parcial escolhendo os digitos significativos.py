#gauss com pivoteamento parcial escolhendo os digitos significativos

import numpy as np

def formatar_com_digitos_significativos(valor, digitos):
    """
    Formata o valor com um número específico de dígitos significativos.
    """
    return f"{valor:.{digitos}g}"

def eliminacao_de_gauss_com_pivoteamento_flutuante(A, b, digitos_significativos=2):
    """
    Resolve um sistema linear Ax = b usando o método de Eliminação de Gauss com pivoteamento parcial,
    com aritmética de ponto flutuante e formatação de dígitos significativos, mostrando todos os passos.

    Parâmetros:
    A (list of lists): Matriz dos coeficientes.
    b (list): Vetor de termos independentes.
    digitos_significativos (int): Número de dígitos significativos para exibição.

    Retorna:
    list: Solução do sistema linear.
    """
    n = len(A)  # Número de equações (linhas da matriz)

    # Convertendo A e b para numpy arrays com tipo ponto flutuante para precisão
    A = np.array(A, dtype=np.float64)
    b = np.array(b, dtype=np.float64)

    print("=== Método de Eliminação de Gauss com Pivoteamento Parcial ===")
    print("Matriz A (coeficientes do sistema):")
    for row in A:
        print("   ", [formatar_com_digitos_significativos(val, digitos_significativos) for val in row])
    print(f"\nVetor b (termos independentes): {[formatar_com_digitos_significativos(val, digitos_significativos) for val in b]}\n")

    # Fase de Eliminação para transformar A em uma matriz triangular superior
    for k in range(n):
        print(f"Passo {k+1}: Trabalhando com a coluna {k}")

        # Pivô parcial: escolher o maior elemento da coluna k para o pivô
        max_index = max(range(k, n), key=lambda i: abs(A[i][k]))
        if np.isclose(A[max_index][k], 0):
            raise ValueError("Sistema sem solução única (zero encontrado na diagonal principal)")

        # Troca de linhas para garantir o maior pivô
        if max_index != k:
            A[[k, max_index]] = A[[max_index, k]]  # Troca de linhas usando numpy
            b[[k, max_index]] = b[[max_index, k]]
            print(f"  - Trocando linha {k} com linha {max_index} para maximizar o pivô")
            print(f"  - Nova Matriz A após troca de linhas:")
            for row in A:
                print("   ", [formatar_com_digitos_significativos(val, digitos_significativos) for val in row])
            print(f"  - Vetor b após troca: {[formatar_com_digitos_significativos(val, digitos_significativos) for val in b]}\n")

        # O elemento pivô é A[k][k]
        pivô = A[k][k]
        print(f"  - Pivô escolhido: A[{k}][{k}] = {formatar_com_digitos_significativos(pivô, digitos_significativos)}\n")

        # Eliminação para zerar os elementos abaixo do pivô
        for i in range(k+1, n):
            fator = A[i][k] / pivô
            print(f"  - Eliminando elemento A[{i}][{k}] com fator: {formatar_com_digitos_significativos(fator, digitos_significativos)}")
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
                print(f"    - Atualizando A[{i}][{j}]: {formatar_com_digitos_significativos(A[i][j], digitos_significativos)}")
            b[i] -= fator * b[k]
            print(f"  - Nova linha {i} de A: {[formatar_com_digitos_significativos(val, digitos_significativos) for val in A[i]]} | Novo b[{i}] = {formatar_com_digitos_significativos(b[i], digitos_significativos)}\n")

    print("=== Matriz Triangular Superior ===")
    for row in A:
        print("   ", [formatar_com_digitos_significativos(val, digitos_significativos) for val in row])
    print(f"Vetor b após eliminação: {[formatar_com_digitos_significativos(val, digitos_significativos) for val in b]}\n")

    # Fase de Substituição Retroativa para resolver o sistema triangular superior
    x = np.zeros(n, dtype=np.float64)
    print(">>> Iniciando a Substituição Retroativa <<<\n")
    for i in range(n-1, -1, -1):
        # Soma dos produtos dos coeficientes com as soluções já calculadas
        soma = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - soma) / A[i][i]
        print(f"Passo {n-i}: Resolvendo para x[{i}]")
        print(f"  - Soma dos produtos das variáveis já calculadas: {formatar_com_digitos_significativos(soma, digitos_significativos)}")
        print(f"  - Calculando x[{i}] usando: (termo independente b[{i}] = {formatar_com_digitos_significativos(b[i], digitos_significativos)} - soma) / coeficiente A[{i}][{i}] = {formatar_com_digitos_significativos(A[i][i], digitos_significativos)}")
        print(f"  - x[{i}] = ({formatar_com_digitos_significativos(b[i], digitos_significativos)} - {formatar_com_digitos_significativos(soma, digitos_significativos)}) / {formatar_com_digitos_significativos(A[i][i], digitos_significativos)} = {formatar_com_digitos_significativos(x[i], digitos_significativos)}\n")

    print("=== Solução Completa do Sistema ===")
    print(f"Vetor solução x: {[formatar_com_digitos_significativos(val, digitos_significativos) for val in x]}")
    return x

# Exemplo de uso:
A = [
    [0.0003, 1.567, 3.1415],   # Coeficientes da primeira equação
    [1.478, 2.718, -0.999],    # Coeficientes da segunda equação
    [3.456, -1.234, 2.345]     # Coeficientes da terceira equação
]
b = [2.718, 3.1415, 1.618]  # Termos independentes correspondentes às equações acima

# Chamando a função para resolver o sistema e imprimir os passos com 8 dígitos significativos
solucao = eliminacao_de_gauss_com_pivoteamento_flutuante(A, b, digitos_significativos=8)
