def invertir_cadena_manual(cadena):
    cadena_invertida = ''
    for letra in cadena: # Recorremos la cadena de texto de adelante hacia atras
        cadena_invertida = letra + cadena_invertida # Concatenamos la letra actual con la cadena invertida
    return cadena_invertida