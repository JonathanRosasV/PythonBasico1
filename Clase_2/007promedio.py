# Este programa lo hice para calcular mi nota final de mis cursos de pregrado

print('Este programa calcula el promedio de notas: \n')
nombre = input('Escribe aqui tu nombre:')

# Pedir la nota del parcial 1 y verificar que esté entre 0 y 20
parcial1 = float(input('Escribe tu nota del parcial 1: '))
if parcial1 < 0 or parcial1 > 20:
    print("Error: La nota debe estar entre 0 y 20. Programa terminado.")
elif (parcial2 := float(input('Escribe tu nota del parcial 2: '))) < 0 or parcial2 > 20:
    print("Error: La nota debe estar entre 0 y 20. Programa terminado.")
elif (final := float(input('Escribe tu nota del final: '))) < 0 or final > 20:
    print("Error: La nota debe estar entre 0 y 20. Programa terminado.")
else:
    # Calcular el promedio
    prom = (parcial1 + parcial2 + final) / 3
    print(f'{nombre}, tu promedio es: {round(prom, 2)}')

    # Queremos que le avisen al alumno si aprobo o no
    if prom < 11:
        print(f'{nombre}, lo sentimos, reprobaste. Tu nota es: {round(prom, 2)}.')
    elif prom == 20:
        print(f'{nombre}, ¡felicitaciones! Has obtenido la máxima nota posible: {round(prom, 2)}.')
    elif prom == 11 and parcial1 < 11:
        print(f'{nombre}, aprobaste con lo justo, pero tu nota del parcial 1 fue baja ({parcial1}).')
    else:
        print(f'{nombre}, felicitaciones, aprobaste. Tu nota es: {round(prom, 2)}.')