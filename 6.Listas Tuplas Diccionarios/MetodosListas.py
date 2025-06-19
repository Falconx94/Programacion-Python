lista=[5 , 4 , 7  , 2 , 15 , 18, 6 , 3 , 1 , 5]

print(lista)

#Agregar valor al final de la LISTA
lista.append(8)
print(lista)
lista.append('Python')
print(lista)

#Ingresar un valor en cierto lugar de la LISTA, primer parametro es la Posición y el segundo parametro el Valor
lista.insert(2 , 2.5)
print(lista)

#Contar valores que se repitan, el paramatro sera el valor a contar
print(lista.count(5))

#Indicar en que posición se encuentra un valor, el paramatro sera el valor a buscar
print(lista.index(4))