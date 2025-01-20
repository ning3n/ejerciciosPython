#/*
#* Crea una función que sume 2 números y retorne su resultado pasados
#* unos segundos.
#* - Recibirá por parámetros los 2 números a sumar y los segundos que
#*   debe tardar en finalizar su ejecución.
#* - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#*   asíncrona, es decir, sin detener la ejecución del programa principal.
#*   Se podría ejecutar varias veces al mismo tiempo.
#*/

import time #importamos la libreria time

def pararTiempo(numero1,numero2,segundos):
    #Esta funcion va a realizar una suma de los dos primeros Enteros pasados como argumentos, y retornara el resultado en tanto tiempo como indique el valor del argumento "segundos"
    while True:
        resultado = numero1 + numero2

        time.sleep(segundos)
        return resultado

if __name__=='__main__':
    print(pararTiempo(4,6,2)) #Imprimimos el resultado de la funcion con los valores de los parametros introducidos