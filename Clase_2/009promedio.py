# Este programa lo hice para calcular mi nota final de mis cursos de pregrado

print('Este programa calcula el promedio de notas: \n')
nombre = input('Escribe aqui tu nombre:')

# Variable para acumular la suma de las notas
suma_notas = 0

# Usamos un for para pedir cada nota y sumar directamente
for i in range(1, 4):
    # Determinar el nombre de la nota según el índice
    if i == 1:
        descripcion = 'parcial 1'
    elif i == 2:
        descripcion = 'parcial 2'
    else:
        descripcion = 'final'
    
    # Solicitar la nota y validar que esté entre 0 y 20
    nota = float(input(f'Escribe tu nota del {descripcion}: '))
    while nota < 0 or nota > 20:
        print("Error: La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        nota = float(input(f'Escribe tu nota del {descripcion}: '))
    
    # Sumar la nota a la acumulación total
    suma_notas += nota

    # Guardar la primera nota para referencia si es necesario
    if i == 1:
        parcial1 = nota

# Calcular el promedio usando el operador walrus directamente en la condición
if (prom := suma_notas / 3) < 11:
    print(f'{nombre}, lo sentimos, reprobaste. Tu nota es: {round(prom, 2)}.')
elif prom == 20:
    print(f'{nombre}, ¡felicitaciones! Has obtenido la máxima nota posible: {round(prom, 2)}.')
elif prom == 11 and parcial1 < 11:
    print(f'{nombre}, aprobaste con lo justo, pero tu nota del parcial 1 fue baja ({parcial1}).')
else:
    print(f'{nombre}, felicitaciones, aprobaste. Tu nota es: {round(prom, 2)}.')