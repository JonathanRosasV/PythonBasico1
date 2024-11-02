# Pedir la cantidad de notas
cantidad = int(input("¿Cuántas notas quieres ingresar? "))

# Variable para acumular la suma de las notas
suma_notas = 0

# Bucle for para ingresar cada nota
for i in range(cantidad):
    # Pedir la nota y validar que esté en el rango 0-20
    nota = float(input(f'Ingresa la nota {i + 1}: '))
    while nota < 0 or nota > 20:
        print("Error: La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        nota = float(input(f'Ingresa la nota {i + 1}: '))
    
    # Sumar la nota a la acumulación total
    suma_notas += nota

# Calcular el promedio
promedio = suma_notas / cantidad

# Imprimir el promedio
print("El promedio de las notas es:", round(promedio, 2))
