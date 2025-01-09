#Generar los primeros 50 numeros de la serie Fibonacci

#Solucion

a = 0
b = 1

print(a, b, end=' ')

for i in range(48):
    a,b = b, a + b
    print(b, end=' ')