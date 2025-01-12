def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal > 0:
        # Se almacena el modulo en el orden correcto
        numero_binario += (numero_decimal % 2) * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario

    # ejemplos de uso

print(decimal_a_binario(5))  # 101
print(decimal_a_binario(35)) # 100011
print(decimal_a_binario(22301)) # 101011011000101