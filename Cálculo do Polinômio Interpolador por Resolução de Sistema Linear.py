import numpy as np

def imprimir_matriz(matriz):
    """
    Função para imprimir uma matriz de forma legível.

    :param matriz: matriz a ser impressa
    """
    for linha in matriz:
        print(" | ".join(f"{num:10.4f}" for num in linha))
    print()

def interpolacao_polinomial(x_values, y_values):
    """
    Função que calcula os coeficientes do polinômio interpolador
    resolvendo um sistema linear e explica cada etapa do processo.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :return: coeficientes do polinômio interpolador
    """
    n = len(x_values)

    # Montando a matriz de Vandermonde
    print("Passo 1: Montando a matriz de Vandermonde...")
    print("Cada elemento da matriz é calculado como x[i] elevado ao índice da coluna.")
    A = np.vander(x_values, increasing=True)
    print("Matriz de Vandermonde construída:")
    imprimir_matriz(A)

    # Resolvendo o sistema linear A * coef = y_values
    print("Passo 2: Resolvendo o sistema linear A * coef = y_values...")
    print("O sistema linear é formado pela multiplicação da matriz de Vandermonde pelos coeficientes do polinômio.")
    print("Sistema linear montado: ")
    for i in range(n):
        equacao = " + ".join(f"{A[i, j]:.4f}*a{j}" for j in range(n))
        print(f"{equacao} = {y_values[i]:.4f}")
    coef = np.linalg.solve(A, y_values)

    # Exibindo os coeficientes do polinômio
    print("\nPasso 3: Coeficientes encontrados (do termo de menor grau para o maior):")
    for i, c in enumerate(coef):
        print(f"a{i} = {c:.4f}")

    return coef

def construir_polinomio(coef):
    """
    Função que constrói a expressão simbólica do polinômio.

    :param coef: coeficientes do polinômio interpolador
    :return: string representando o polinômio interpolador
    """
    n = len(coef)
    termos = []
    for i in range(n):
        termo = f"{coef[i]:.4f}"
        if i == 1:
            termo += "x"
        elif i > 1:
            termo += f"x^{i}"
        termos.append(termo)

    polinomio = " + ".join(termos[::-1])
    return polinomio.replace("+ -", "- ")

def main():
    # Solicita ao usuário os valores de x e f(x)
    n = int(input("Quantos pontos você deseja inserir? "))

    x_values = []
    y_values = []

    for i in range(n):
        x = float(input(f"Digite o valor de x{i+1}: "))
        y = float(input(f"Digite o valor de f(x{i+1}): "))
        x_values.append(x)
        y_values.append(y)

    # Calcula os coeficientes do polinômio interpolador explicando o processo
    coef = interpolacao_polinomial(x_values, y_values)

    # Constroi e exibe o polinômio interpolador
    polinomio = construir_polinomio(coef)
    print("\nPasso 4: Polinômio interpolador final:")
    print(polinomio)

if __name__ == "__main__":
    main()

