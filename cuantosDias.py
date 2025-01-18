#programa que calcula y retorna cuantos dias hay entre dos cadenas de texto que representan fechas

def cuantosDias(fecha1, fecha2):
    #separar las fechas en listas
    fecha1 = fecha1.split("/")
    fecha2 = fecha2.split("/")
    #convertir a enteros
    for i in range(3):
        fecha1[i] = int(fecha1[i])
        fecha2[i] = int(fecha2[i])
    #calcular los dias
    dias = 0
    #calcular los dias del primer año
    dias += 365 - fecha1[0]
    #calcular los dias del segundo año
    dias += fecha2[0]
    #calcular los dias de los meses
    diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    #calcular los dias de los meses del primer año
    for i in range(fecha1[1]-1):
        dias += diasMeses[i]
    #calcular los dias de los meses del segundo año
    for i in range(fecha2[1]-1):
        dias += diasMeses[i]
    #calcular los dias de los dias
    dias += fecha2[2] - fecha1[2]
    return dias

fecha1 = input("Introduce la primera fecha (dd/mm/aaaa): ")
fecha2 = input("Introduce la segunda fecha (dd/mm/aaaa): ")
print(cuantosDias(fecha1, fecha2))

