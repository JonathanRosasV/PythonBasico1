# Función para pedir una nota y validar que esté entre 0 y 20
def pedir_nota(examen):
    nota = float(input(f'Escribe tu nota del {examen}: '))
    while nota < 0 or nota > 20:
        print("Error: La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        nota = float(input(f'Escribe tu nota del {examen}: '))
    return nota

# Función para calcular el promedio y mostrar el resultado
def calcular_promedio(nombre, parcial1, parcial2, final):
    prom = (parcial1 + parcial2 + final) / 3
    # Determinar el mensaje de aprobación o reprobación
    if prom < 11:
        print(f'{nombre}, lo sentimos, reprobaste. Tu nota es: {round(prom, 2)}.')
    elif prom == 20:
        print(f'{nombre}, ¡felicitaciones! Has obtenido la máxima nota posible: {round(prom, 2)}.')
    elif prom == 11 and parcial1 < 11:
        print(f'{nombre}, aprobaste con lo justo, pero tu nota del parcial 1 fue baja ({parcial1}).')
    else:
        print(f'{nombre}, felicitaciones, aprobaste. Tu nota es: {round(prom, 2)}.')

# Programa principal
print('Este programa calcula el promedio de notas:\n')
nombre = input('Escribe aquí tu nombre: ')

# Pedir cada una de las notas usando la función pedir_nota
parcial1 = pedir_nota('parcial 1')
parcial2 = pedir_nota('parcial 2')
final = pedir_nota('examen final')

# Calcular el promedio y mostrar el resultado
calcular_promedio(nombre, parcial1, parcial2, final)
