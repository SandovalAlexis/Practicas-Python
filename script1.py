# Precio Articulo

# Ambiente

# Variables Reales
#c = float
#p = float

# Constante Real
#r = float

# Variable Entera
#n, a = int

# Ciclo Principal

print("*************************************************************************")
print("Este programa permite calcular el precio de un articulo para un año dado")
print("*************************************************************************")
print()
print("Por favor, ingrese el valor actual del articulo")
c = int(input())
print("A hora ingrese el año actual y el año siguiente")
a = int(input())
n = int(input())

# Constante
r = 0.04

# Calculo operacional
potencia = (n - a)
suma = (1 + r)
incremento = float(c * suma)
Precio = incremento ** potencia

# Mostramos Resultados Finales
print(" El precio del articulo en el año ", a, "es de ", Precio)
