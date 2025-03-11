import numpy as np
import matplotlib.pyplot as plt

def interpolacao_polinomial(x_values, y_values):
    """
    Função que calcula os coeficientes do polinômio interpolador
    resolvendo um sistema linear.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :return: coeficientes do polinômio interpolador
    """
    n = len(x_values)
    # Montando a matriz de Vandermonde
    A = np.vander(x_values, increasing=True)
    # Resolvendo o sistema linear A * coef = y_values para obter os coeficientes
    coef = np.linalg.solve(A, y_values)
    return coef

def avalia_polinomio(coef, x):
    """
    Função que avalia o polinômio nos valores de x.

    :param coef: coeficientes do polinômio interpolador
    :param x: valor ou valores onde se quer avaliar o polinômio
    :return: valor ou valores do polinômio em x
    """
    return np.polyval(coef[::-1], x)

def plot_interpolation(x_values, y_values, coef):
    """
    Função que plota o polinômio interpolador junto com os pontos dados.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :param coef: coeficientes do polinômio interpolador
    """
    x_min, x_max = min(x_values), max(x_values)
    x_plot = np.linspace(x_min, x_max, 500)
    y_plot = avalia_polinomio(coef, x_plot)

    plt.plot(x_plot, y_plot, label='Polinômio Interpolador', color='blue')
    plt.scatter(x_values, y_values, color='red', label='Pontos Dados')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolação Polinomial')
    plt.legend()
    plt.grid(True)
    plt.show()

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

    # Calcula os coeficientes do polinômio interpolador
    coef = interpolacao_polinomial(x_values, y_values)

    # Exibe os coeficientes do polinômio
    print("\nCoeficientes do polinômio interpolador (do termo de menor grau para o maior):")
    print(coef)

    # Plota o polinômio interpolador
    plot_interpolation(x_values, y_values, coef)

if __name__ == "__main__":
    main()
