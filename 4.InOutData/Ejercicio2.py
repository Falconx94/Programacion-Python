#Logica del ejercicio
practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))
ExamenParcial = float(input('Ingrese el valor del examen parcial: '))
ExamenFinal = float(input('Ingrese el valor del examen final: '))

PromedioPractica = (practica1+practica2+practica3)/3
PromedioFinal = (PromedioPractica+(2*ExamenParcial)+(3*ExamenFinal))/6
print('El Promedio de Practica del estudiante es:\n ',PromedioPractica,'\nY el promedio Final es de: ',PromedioFinal)

'''
#Logica Personal
p1 = float(input('Ingrese promedio parcial1: '))
p2 = float(input('Ingrese promedio parcial2: '))
p3 = float(input('Ingrese promedio parcial3: '))
ep = float(input('Ingrese promedio examen parcial: '))
ef = float(input('Ingrese promedio examen final: '))

pp = (p1+p2+p3)/3
prom = (pp+(2*ep)+(3*ef))/6
print('El Promedio parcial es: ',pp,'\nEl promedio general es: ',prom)'''