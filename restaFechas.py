from datetime import datetime, timedelta

def calcular_dias(fecha1, fecha2):
    formato = "%d/%m/%Y"
    fecha1 = datetime.strptime(fecha1, formato)
    fecha2 = datetime.strptime(fecha2, formato)
    diferencia = fecha2 - fecha 1
    return diferencia.days

fecha1 = input("Fecha 1: ")
fecha2 = input("Fecha 2: ")
dias = calcular_dias(fecha1, fecha2)
print("Diferencia en días:", dias)