#Programa que recibe un string y convierte la primera letra a mayuscula

def aMayuscula(cadena):
    return cadena[0].upper() + cadena[1:]

cadena = input("Introduce una cadena: ")
print(aMayuscula(cadena))