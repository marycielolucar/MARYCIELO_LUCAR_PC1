texto_modificar = input("Ingrese un texto: ")
vocales = "aeiouAEIOU"
texto_sin_vocales = "".join([c for c in texto_modificar if c not in vocales])
print(texto_sin_vocales)