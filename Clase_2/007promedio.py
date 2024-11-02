# Este programa lo hice para calcular mi nota final de mis cursos de pregrado

print('Este programa calcula el promedio de notas: \n')
nombre = input('Escribe aqui tu nombre:')

parcial1 = float(input('Escribe tu nota del parcial 1:'))
while parcial1 < 0 or parcial1 > 20:
    print("La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
    parcial1 = float(input('Escribe tu nota del parcial 1:'))

parcial2 = float(input('Escribe tu nota del parcial 2:'))
while parcial2 < 0 or parcial2 > 20:
    print("La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
    parcial2 = float(input('Escribe tu nota del parcial 2:'))

final = float(input('Escribe tu nota del final:'))
while final < 0 or final > 20:
    print("La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
    final = float(input('Escribe tu nota del final:'))

prom = (parcial1 + parcial2 + final) / 3

print(f'{nombre}, tu promedio es:', round(prom,2) )

# Queremos que le avisen al alumno si aprobo o no
if (prom<11):
    print(f'{nombre}, lo sentimos, reprobaste. Tu nota es: {round(prom,2)}.')
else:
    print(f'{nombre}, felicitaciones, aprobaste. Tu nota es: {round(prom,2)}.')