char = input('Ingrese una letra: \n')
char2 = input('Ingrese otra letra: \n')

if(char == 'a' or char =='e' or char=='i' or char=='o' or char=='u'):
    if char2.isupper():
        print(char.upper,char2.lower)
    else:
        print(char.upper(),char2)
else:
    print(char, char2)