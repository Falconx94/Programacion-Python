nombre = input ('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

#Impresión basica
print(nombre)
print(edad)
 
#Impresión Concatenada
print(nombre + str(edad))
print(nombre, edad)

#Sustitución por valor de variables
print('Hola {} tienes {}'.format(nombre, edad))