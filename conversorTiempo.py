#/*
#* Crea una función que reciba días, horas, minutos y segundos (como enteros)
#* y retorne su resultado en milisegundos.
#*/

def conversorTiempo(dias,horas,minutos,segundos): # la funcion creada recibira como argumento los valores correspondientes a estos 4 parametros

    tiempoTotal = 0  #Inicializamos el tiempo inicial a 0
    tiempoTotal += dias*(3600*24*1000) #iremos aumentando el valor de tiempoTotal en funcion del valor del parametro
    tiempo total += horas*(3600*1000) #multiplicado por los milisegundos en cuestion
    tiempoTotal += minutos*(60*1000) #y asi con el resto de parametros
    tiempoTotal += segundos*1000

    return 'En el tiempo introducido, han transcurrido {} milisegundos'.format(tiempoTotal) #Finalmente, hacemos que la funcion retorne un string
                                                                                            #con el valor de tiempoTotal

if __name__=='__main__':
    print(conversorTiempo(0,0,0,1)) #Imprimimos el resultado de la funcion con los valores de los parametros introducidos