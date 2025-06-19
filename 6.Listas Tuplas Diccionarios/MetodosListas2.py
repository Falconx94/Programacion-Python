#Hacer que la lista se ordene de meno a mayor
lista=[5 , 4 , 7  , 2 , 15 , 18, 6 , 3 , 1]

print(lista)
lista.sort(reverse=False) #Es necesario decirle en que sentido ordenara los valores, En este caso ascendente
print(lista)

#Voltea el orden de la lista sin ascendente o descendente
lista.reverse()
print(lista)