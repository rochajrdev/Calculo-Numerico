import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iterativo_linear(g, x0, max_iter, E):
    k = 0
    erro = float('inf')
    xk = x0

    print(f"Iniciando iteração com x0 = {x0}\n")

    while k < max_iter and erro > E:
        xk_next = g(xk)
        erro = abs(xk_next - xk)

        print(f"Iteração {k}:")
        print(f"\tPasso 1: xk = {xk}")
        print(f"\tPasso 2: g(xk) = {xk_next}")
        print(f"\tPasso 3: Erro = |xk_next - xk| = {erro}\n")

        if erro < E:
            print(f"Convergência alcançada:")
            print(f"\t- xk = {xk_next}")
            print(f"\t- Erro = {erro}\n")
            return xk_next, k, erro

        xk = xk_next
        k += 1

    print(f"Número máximo de iterações atingido:")
    print(f"\t- xk = {xk}")
    print(f"\t- Erro = {erro}\n")
    return xk, k, erro

def main():
    def g(x):
        # Defina a função g(x) que representa a transformação do método do ponto fixo
        return np.sqrt(np.sin(x) + 1)

    x0 = 0.5  # Ponto inicial
    E = 1e-5  # Tolerância de erro
    max_iter = 100  # Número máximo de iterações

    try:
        zero, iteracoes, erro = iterativo_linear(g, x0, max_iter, E)
        print(f"Zero da função: {zero:.6f}")
        print(f"Número de iterações: {iteracoes}")
        print(f"Erro final: {erro:.6f}")
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
