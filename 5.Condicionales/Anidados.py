nombre = 'Juan'
edad = 18

if nombre == 'Juan':
    if edad >= 18:
        print('Tu eres {} y tienes mayoria de edad',format(nombre))
    else:
        print('Tu eres {} pro no eres mayor de edad',format(nombre))
else:
    if(edad >=18):
        print('Tu no eres {} y tampoco eres mayor de edad',format(nombre))
    else:
        print('Tu no eres {}, pero estas vajo vigilancia',format(nombre))