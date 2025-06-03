from math import sqrt
#Logica del ejercicio

A = float(input('Ingrese valor de a: '))
B = float(input('Ingrese valor de b: '))
C = float(input('Ingrese valor de c: '))
x1=0
x2=0

if((B**2)-(4*A*C)) < 0:
    print('El resultado es negativo, no se puede sacar raiz')
else:
    x1= (-B + sqrt(((B**2)-(4*A*C))))/(2*A)
    x2= (-B - sqrt(((B**2)-(4*A*C))))/(2*A)

print('\nEl resultado de X1 es: ',x1)
print('\nEl resultado de X2 es: ',x2)

'''
#Logica personal
A = float(input('Ingrese valor de a: '))
B = float(input('Ingrese valor de b: '))
C = float(input('Ingrese valor de c: '))

Bn = B*-1 #B negativo
D = B**2 #B al cuadrado
E = 4*(A*C) 
F = 2*A 
G = D-E #(B^2)-4AC
H = sqrt(G) #Raiz de G
I = Bn+H
J = Bn-H
X1= I/F
X2= J/F

print('El resultado de X1 es: ',X1)
print('El resultado de X2 es: ',X2)'''