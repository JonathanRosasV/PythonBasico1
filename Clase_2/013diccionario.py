calificaciones = {
    "Ana": [15, 18, 20],
    "Luis": [14, 16, 17]
}

# Calcular y mostrar el promedio de cada estudiante
for nombre, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

