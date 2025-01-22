# Crea dos funciones, una que calcule el maximo comun divisor y otra que calcule el minimo comun multiplo de dos numeros.

def maximoComunDivisor(numero1,numero2):
    maximoDivisor_numero1 = []

    contador1 = 1
    while contador1 < numero1:
        if num1 % contador1 == 0:
            maximoDivisor_numero1.append(contador1)
            contador1 += 1                              #Como el numero que guarda la variable contador1 es divisor de numero1
            continue                                    #lo añadimos a la lista maximoDivisor_numero1
        else:
            contador1 += 1
            continue

    maximoDivisor_numero2 = []

    contador2 = 1
    while contador2 < numero2:
        if num2 % contador2 == 0:
            maximoDivisor_numero2.append(contador2)
            contador2 += 1                              #Como el numero que guarda la variable contador2 es divisor de numero2
            continue                                    #lo añadimos a la lista maximoDivisor_numero2
        else:
            contador2 += 1
            continue

    divisoresComunes = []

    for numero in maximoDivisor_numero1:
        for numero2 in maximoDivisor_numero2:
            if numero == numero2:
                divisoresComunes.append(numero)        #En este bucle for, comprobamos si hay divisores comunes entre los dos numeros
    
    resultado = max(divisoresComunes)                  #El resultado sera el mayor de los divisores comunes

    return 'El maximo comun divisor de {} y {} es {}'.format(numero1,numero2,resultado)

#Ahora, creamos la funcion que calcule el minimo comun multiplo de dos numeros

def minimoComunMultiplo(numero1,numero2):
    """funcion que calcula el minimo comun multiplo de dos numeros"""

    minimoMultiplo_numero1 = []

    for multiplo1 in range(1,20):
        minimoMultiplo_numero1.append(numero1*multiplo1)

    minimoMultiplo_numero2 = []

    for multiplo2 in range(1,20):
        minimoMultiplo_numero2.append(multiplo2*numero2)
        
    multiplosComunes = []

    for numero in minimoMultiplo_numero1:
        for numero2 in minimoMultiplo_numero2:
            if numero == numero2:
                multiplosComunes.append(numero)         #En este bucle for, comprobamos si hay multiplos comunes entre los dos numeros

    resultado = min(multiplosComunes)                  #El resultado sera el menor de los multiplos comunes

    return 'El minimo comun multiplo de {} y {} es {}'.format(numero1,numero2,resultado)

if __name__=='__main__':
    print(maximoComunDivisor(15,20)) #Imprimimos el resultado de la funcion con los valores de los parametros introducidos
    print(minimoComunMultiplo(3,4)) #Imprimimos el resultado de la funcion con los valores de los parametros introducidos