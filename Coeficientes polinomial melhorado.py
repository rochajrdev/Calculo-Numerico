import numpy as np  # Importa a biblioteca NumPy, que oferece suporte para arrays e operações matemáticas.
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para criar gráficos.

def interpolacao_polinomial(x_values, y_values):
    """
    Função que calcula os coeficientes do polinômio interpolador
    resolvendo um sistema linear.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :return: coeficientes do polinômio interpolador
    """
    n = len(x_values)  # Obtém o número de pontos (quantidade de valores em x_values).
    # Montando a matriz de Vandermonde
    A = np.vander(x_values, increasing=True)  # Cria a matriz de Vandermonde para os valores de x.
    # Resolvendo o sistema linear A * coef = y_values para obter os coeficientes
    coef = np.linalg.solve(A, y_values)  # Resolve o sistema linear para encontrar os coeficientes do polinômio.
    return coef  # Retorna os coeficientes encontrados.

def avalia_polinomio(coef, x):
    """
    Função que avalia o polinômio nos valores de x.

    :param coef: coeficientes do polinômio interpolador
    :param x: valor ou valores onde se quer avaliar o polinômio
    :return: valor ou valores do polinômio em x
    """
    return np.polyval(coef[::-1], x)  # Avalia o polinômio nos valores de x usando os coeficientes fornecidos.

def constroi_polinomio(coef):
    """
    Função que constrói a expressão simbólica do polinômio.

    :param coef: coeficientes do polinômio interpolador
    :return: string representando o polinômio interpolador
    """
    n = len(coef)  # Obtém o número de coeficientes.
    termos = []  # Inicializa uma lista para armazenar os termos do polinômio.
    for i in range(n):
        termo = f"{coef[i]:.4f}"  # Formata o coeficiente atual com 4 casas decimais.
        if i == 1:
            termo += "x"  # Adiciona 'x' se for o termo linear.
        elif i > 1:
            termo += f"x^{i}"  # Adiciona 'x^i' se for um termo de grau maior que 1.
        termos.append(termo)  # Adiciona o termo à lista de termos.

    polinomio = " + ".join(termos[::-1])  # Junta os termos na forma de uma expressão polinomial.
    return polinomio.replace("+ -", "- ")  # Substitui '+ -' por '-' para formatar corretamente o polinômio.

def plot_interpolation(x_values, y_values, coef):
    """
    Função que plota o polinômio interpolador junto com os pontos dados.

    :param x_values: lista com os valores de x
    :param y_values: lista com os valores de f(x)
    :param coef: coeficientes do polinômio interpolador
    """
    x_min, x_max = min(x_values), max(x_values)  # Define o intervalo de x para o gráfico.
    x_plot = np.linspace(x_min, x_max, 500)  # Gera 500 pontos igualmente espaçados no intervalo de x.
    y_plot = avalia_polinomio(coef, x_plot)  # Avalia o polinômio nos pontos gerados.

    plt.plot(x_plot, y_plot, label='Polinômio Interpolador', color='blue')  # Plota o polinômio interpolador.
    plt.scatter(x_values, y_values, color='red', label='Pontos Dados')  # Plota os pontos originais.
    plt.xlabel('x')  # Define o rótulo do eixo x.
    plt.ylabel('f(x)')  # Define o rótulo do eixo y.
    plt.title('Interpolação Polinomial')  # Define o título do gráfico.
    plt.legend()  # Exibe a legenda no gráfico.
    plt.grid(True)  # Adiciona uma grade ao gráfico.
    plt.show()  # Mostra o gráfico.

def main():
    # Solicita ao usuário os valores de x e f(x)
    n = int(input("Quantos pontos você deseja inserir? "))  # Pergunta ao usuário quantos pontos ele deseja inserir.

    x_values = []  # Inicializa a lista para armazenar os valores de x.
    y_values = []  # Inicializa a lista para armazenar os valores de f(x).

    for i in range(n):
        x = float(input(f"Digite o valor de x{i+1}: "))  # Solicita o valor de x ao usuário.
        y = float(input(f"Digite o valor de f(x{i+1}): "))  # Solicita o valor de f(x) ao usuário.
        x_values.append(x)  # Adiciona o valor de x à lista x_values.
        y_values.append(y)  # Adiciona o valor de f(x) à lista y_values.

    # Calcula os coeficientes do polinômio interpolador
    coef = interpolacao_polinomial(x_values, y_values)  # Chama a função para calcular os coeficientes do polinômio.

    # Exibe os coeficientes do polinômio
    print("\nCoeficientes do polinômio interpolador (do termo de menor grau para o maior):")
    print(coef)  # Imprime os coeficientes do polinômio.

    # Constroi e exibe o polinômio interpolador
    polinomio = constroi_polinomio(coef)  # Constrói o polinômio como uma expressão matemática.
    print("\nPolinômio interpolador:")
    print(polinomio)  # Imprime o polinômio interpolador.

    # Plota o polinômio interpolador
    plot_interpolation(x_values, y_values, coef)  # Chama a função para plotar o polinômio e os pontos dados.

if __name__ == "__main__":
    main()  # Chama a função main() se o script for executado diretamente.
