cad1 = input('Ingrese la primer palabra:\n')
cad2 = input('Ingrese la segunda palabra:\n')

if ((len(cad1))<3 or (len(cad2))<3):
    print('Una de las palabras es muy corta no rimaran')
elif (cad1[-3: ] == cad2[-3: ]):
    print('Las Palabras Riman')
else:
    print('Las palabras NO riman')