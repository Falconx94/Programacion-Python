lista = ['Python' , 24, 'Nombre','Alexander', 4.14 , 6,28]

#Modificar datos
print(lista)
lista[3] = 'Terry'
print(lista)

#Eliminar datos
lista.pop()#Eliminar ultimo valor
print(lista)

lista.remove('Python') #Elimina el valor establecido como parametro
print(lista)