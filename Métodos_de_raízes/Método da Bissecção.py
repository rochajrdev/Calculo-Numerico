import math
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def bisseccao(f, a, b, max_iter, E):
    if a >= b:
        raise ValueError("O extremo esquerdo do intervalo (a) deve ser menor que o extremo direito (b).")
    if f(a) * f(b) > 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")

    nit = int(np.ceil((np.log(b - a) - np.log(E)) / np.log(2)))
    print(f"Número estimado de iterações necessárias: {nit}\n")

    k = 0
    fa = f(a)
    erro = float('inf')

    while k <= min(nit, max_iter):
        xk = (a + b) / 2
        fxk = f(xk)

        print(f"Iteração {k}:")
        print(f"\tPasso 1: O intervalo atual é [{a}, {b}]")
        print(f"\tPasso 2: O ponto médio é xk = (a + b) / 2 = ({a} + {b}) / 2 = {xk}")
        print(f"\tPasso 3: Calculamos f(a) = {fa} e f(xk) = {fxk}")
        print(f"\tPasso 4: Verificamos se f(xk) é aproximadamente zero ou se o intervalo é suficientemente pequeno.")

        if fxk == 0 or abs(b - a) < E:
            erro = abs(b - a)
            print(f"\tConvergência alcançada:")
            print(f"\t\t- Ponto médio (xk) = {xk}")
            print(f"\t\t- f(xk) = {fxk}")
            print(f"\t\t- Erro = {erro}\n")
            return xk, k, erro

        k += 1
        if fa * fxk > 0:
            a = xk
            fa = fxk
            print(f"\tPasso 5: Como f(a) * f(xk) > 0, atualizamos a = xk = {a}")
        else:
            b = xk
            print(f"\tPasso 5: Como f(a) * f(xk) <= 0, atualizamos b = xk = {b}")

        print(f"\tNovo intervalo: [{a}, {b}]\n")

    erro = abs(b - a)
    print(f"Número máximo de iterações atingido:")
    print(f"\t- Ponto médio (xk) = {xk}")
    print(f"\t- Erro = {erro}\n")
    return xk, k, erro

def main():
    def f(x):
        return x**3 - 9*x + 3

    a = 0
    b = 1
    E = 0.001
    max_iter = 100

    try:
        zero, iteracoes, erro = bisseccao(f, a, b, max_iter, E)
        print(f"Zero da função: {zero}")
        print(f"Número de iterações: {iteracoes}")
        print(f"Erro final: {erro}")
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()