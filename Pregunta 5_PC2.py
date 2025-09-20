numeros_usuario = []
while True:
    solicitud = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    if solicitud == "NO":
        break
    num = int(input("Ingrese el número: "))
    numeros_usuario.append(num)

pares = sum(1 for n in numeros_usuario if n % 2 == 0)
impares = len(numeros_usuario) - pares

print("Números ingresados:", numeros_usuario)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)