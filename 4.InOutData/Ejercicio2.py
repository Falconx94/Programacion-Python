#Logica Personal
p1 = float(input('Ingrese promedio parcial1: '))
p2 = float(input('Ingrese promedio parcial2: '))
p3 = float(input('Ingrese promedio parcial3: '))
ep = float(input('Ingrese promedio examen parcial: '))
ef = float(input('Ingrese promedio examen final: '))

pp = (p1+p2+p3)/3
prom = (pp+(2*ep)+(3*ef))/6
print('El promedio general es: ',prom)