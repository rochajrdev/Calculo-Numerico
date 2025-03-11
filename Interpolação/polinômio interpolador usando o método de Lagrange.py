import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, expand

def formatar_com_digitos_significativos(valor, digitos):
    """
    Formata o valor com um número específico de dígitos significativos.
    """
    return f"{valor:.{digitos}g}"

def polinomio_lagrange(x_values, y_values, digitos_significativos=6):
    """
    Função que calcula o polinômio interpolador usando o método de Lagrange.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :param digitos_significativos: número de dígitos significativos para formatação
    :return: função que avalia o polinômio de Lagrange e a expressão do polinômio
    """
    x = symbols('x')  # Define a variável simbólica x
    n = len(x_values)

    def L(k, x):
        """
        Calcula o k-ésimo polinômio base de Lagrange.

        :param k: índice do polinômio base
        :param x: valor onde avaliar o polinômio base
        :return: valor do polinômio base L_k(x)
        """
        terms = [(x - x_values[j]) / (x_values[k] - x_values[j]) for j in range(n) if j != k]
        L_k = np.prod(terms, axis=0)
        return L_k

    # Inicializa o polinômio como uma soma de zero
    P = 0

    print("\nCalculando o polinômio de Lagrange:")
    # Soma os termos de Lagrange multiplicados pelos valores de y
    for k in range(n):
        L_k = L(k, x)
        P += y_values[k] * L_k
        print(f"\nL_{k}(x) = {' * '.join([f'(x - {x_values[j]}) / ({x_values[k]} - {x_values[j]})' for j in range(n) if j != k])}")
        print(f"   L_{k}(x) = {simplify(L_k)}")
        print(f"   y_{k} * L_{k}(x) = {formatar_com_digitos_significativos(y_values[k], digitos_significativos)} * {simplify(L_k)}")

    # Expande e simplifica o polinômio
    P_expanded = expand(P)
    P_simplified = simplify(P_expanded)
    print("\nPolinômio interpolador simplificado:")
    print(P_simplified)

    # Converte o polinômio simplificado para uma string
    polinomio_exp = str(P_simplified)

    def P_func(x_val):
        """
        Função para avaliar o polinômio interpolador em um valor x_val.

        :param x_val: valor onde avaliar o polinômio
        :return: valor do polinômio interpolador em x_val
        """
        return float(P_simplified.subs(x, x_val))

    return P_func, polinomio_exp

def plot_interpolation(x_values, y_values, P_func):
    """
    Função que plota o polinômio interpolador de Lagrange junto com os pontos dados.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :param P_func: função que avalia o polinômio interpolador
    """
    x_min, x_max = min(x_values), max(x_values)
    x_plot = np.linspace(x_min, x_max, 500)
    y_plot = np.array([P_func(x_val) for x_val in x_plot])

    plt.plot(x_plot, y_plot, label='Polinômio Interpolador', color='blue')
    plt.scatter(x_values, y_values, color='red', label='Pontos Dados')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolação Polinomial de Lagrange')
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

    # Calcula o polinômio interpolador de Lagrange
    P_func, polinomio_exp = polinomio_lagrange(x_values, y_values)

    # Exibe a expressão do polinômio
    print("\nPolinômio interpolador de Lagrange:")
    print(polinomio_exp)

    # Plota o polinômio interpolador
    plot_interpolation(x_values, y_values, P_func)

if __name__ == "__main__":
    main()
