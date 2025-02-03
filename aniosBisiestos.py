#/*
# Crea una funcion que imprima los proximos 30 años bisiestos
# siguientes a uno dado
# Utiliza el menor numero de lineas para resolver el ejercicio
#*/


def comprobarBisiesto(lista):
    for anio in lista:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            print(anio)
        else:
            print('No es bisiesto')

if __name__ == "__main__":
    anio = int(input("Introduce un año: "))
    lista = [anio + i for i in range(1, 31)]
    comprobarBisiesto(lista)