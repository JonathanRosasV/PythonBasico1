# Este programa lo hice para calcular mi nota final de mis cursos de pregrado

print('Este programa calcula el promedio de notas: /n')
nombre = input('Escribe aqui tu nombre:')

parcial1 = float(input('Escribe tu nota del parcial 1:'))
parcial2 = float(input('Escribe tu nota del parcial 2:'))
final = float(input('Escribe tu nota del final:'))

prom = (parcial1 + parcial2 + final) / 3

print(f'{nombre}, tu promedio es:', round(prom,2) )