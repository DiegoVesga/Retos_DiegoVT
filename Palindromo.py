palabra = input("Ingrese una frase o una palabra: ")
palabraf = palabra.replace(" ", "")
palabraf=palabraf.lower()
if palabraf [::-1] == palabraf:
    print("La palabra/frase SI es un palindromo ")
else:
    print("la palabra/frase NO es un palindromo ") 
    