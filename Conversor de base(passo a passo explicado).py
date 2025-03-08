def converter_base_passo_a_passo(numero, base_origem, base_destino):
    # 1. Separação da Parte Inteira e Fracionária
    parte_inteira, separador, parte_fracionaria = numero.partition('.')

    print(f"Parte inteira: {parte_inteira}, Parte fracionária: {parte_fracionaria}\n")

    # 2. Conversão da Parte Inteira da Base de Origem para Decimal
    def int_para_decimal_passo_a_passo(numero, base_origem):
        decimal = 0
        print(f"Convertendo a parte inteira '{numero}' da base {base_origem} para decimal:")
        for i, digito in enumerate(reversed(numero)):
            valor_digito = int(digito, base_origem)
            contribuicao = valor_digito * (base_origem ** i)
            decimal += contribuicao
            print(f"  - Passo {i + 1}: {digito} * {base_origem}^{i} = {contribuicao}")
        print(f"Resultado da parte inteira em decimal: {decimal}\n")
        return decimal

    # 3. Conversão da Parte Fracionária da Base de Origem para Decimal
    def frac_para_decimal_passo_a_passo(numero, base_origem):
        decimal = 0
        print(f"Convertendo a parte fracionária '{numero}' da base {base_origem} para decimal:")
        for i, digito in enumerate(numero):
            valor_digito = int(digito, base_origem)
            contribuicao = valor_digito / (base_origem ** (i + 1))
            decimal += contribuicao
            print(f"  - Passo {i + 1}: {digito} / {base_origem}^{i + 1} = {contribuicao}")
        print(f"Resultado da parte fracionária em decimal: {decimal}\n")
        return decimal

    # 4. Conversão da Parte Inteira de Decimal para a Base Destino
    def de_decimal_para_int_passo_a_passo(decimal, base_destino):
        if decimal == 0:
            return '0'
        digitos = []
        print(f"Convertendo a parte inteira '{decimal}' de decimal para a base {base_destino}:")
        contador_de_passos = 1
        while decimal:
            resto = decimal % base_destino
            novo_decimal = decimal // base_destino
            digitos.append(resto)
            print(f"  - Passo {contador_de_passos}: {decimal} // {base_destino} = {novo_decimal}, resto = {resto}")
            decimal = novo_decimal
            contador_de_passos += 1
        digitos.reverse()
        resultado = ''.join(str(digito) if digito < 10 else chr(digito + 87) for digito in digitos)
        return resultado

    # 5. Conversão da Parte Fracionária de Decimal para a Base Destino
    def de_decimal_para_frac_passo_a_passo(decimal, base_destino, precisao=10):
        digitos = []
        print(f"Convertendo a parte fracionária '{decimal}' de decimal para a base {base_destino}:")
        contador_de_passos = 1
        while decimal != 0 and len(digitos) < precisao:
            decimal *= base_destino
            digito = int(decimal)
            decimal -= digito
            digitos.append(digito)
            print(f"  - Passo {contador_de_passos}: multiplicação = {decimal + digito}, dígito = {digito}, novo decimal = {decimal}")
            contador_de_passos += 1
        resultado = ''.join(str(digito) if digito < 10 else chr(digito + 87) for digito in digitos)
        return resultado

    # Converter parte inteira para decimal
    numero_decimal_inteira = int_para_decimal_passo_a_passo(parte_inteira, base_origem)
    
    # Converter parte fracionária para decimal apenas se existir
    if parte_fracionaria:
        numero_decimal_fracionaria = frac_para_decimal_passo_a_passo(parte_fracionaria, base_origem)
        numero_convertido_fracionaria = de_decimal_para_frac_passo_a_passo(numero_decimal_fracionaria, base_destino)
        resultado_final = de_decimal_para_int_passo_a_passo(int(numero_decimal_inteira), base_destino) + '.' + numero_convertido_fracionaria
    else:
        # Se não houver parte fracionária, apenas converter a parte inteira
        resultado_final = de_decimal_para_int_passo_a_passo(int(numero_decimal_inteira), base_destino)

    print(f"\nO número {numero} na base {base_origem} é {resultado_final} na base {base_destino}")

def validar_numero(numero, base):
    digitos_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    for digito in numero.upper():
        if digito != '.' and digito not in digitos_validos:
            return False
    return True

# Modificar a parte que solicita a entrada do usuário
numero = input("Digite o número que deseja converter (pode incluir parte fracionária): ")
base_origem = int(input("Digite a base atual do número (2-36): "))

# Validar o número antes de continuar
while not validar_numero(numero.split('.')[0], base_origem):
    print(f"Erro: O número contém dígitos inválidos para a base {base_origem}")
    print(f"Dígitos válidos para base {base_origem}: {' '.join('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base_origem])}")
    numero = input("Digite o número novamente: ")

base_destino = int(input("Digite a base para a qual deseja converter (2-36): "))

# Calcular e exibir o resultado com passo a passo
converter_base_passo_a_passo(numero, base_origem, base_destino)