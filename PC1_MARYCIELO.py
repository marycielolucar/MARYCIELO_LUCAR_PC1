#### Variables #######3##################################################################

#### Problema 1
nombre_usuario = input("Ingrese su nombre de usuario: ")
print(f"¡Hola {nombre_usuario}!")

#### Problema 2
monto_consumo = float(input("\nIngrese el total de su consumo en el restaurante: "))
propina = float(input("¿Qué porcentaje de propina desea dejar?: "))
monto_propina = monto_consumo * (propina / 100)
print(f"El cliente debe dejar {monto_propina:.2f} de propina.")

#### Problema 3
payasos_compra = int(input("\nIngrese el número de payasos vendidos: "))
munecas_compra = int(input("Ingrese el número de muñecas vendidas: "))
peso_paquete_total = payasos_compra * 112 + munecas_compra * 75
print(f"El peso total del paquete a transportar es {peso_paquete_total} gramos.")

#### Problema 4
numero_calcular = int(input("\nIngrese un número entero positivo N: "))
suma_numero = numero_calcular * (numero_calcular + 1) // 2
print(f"La suma de los enteros desde 1 hasta {numero_calcular} es: {suma_numero}")

#### Condicionales ##################################################################

#### Problema 5
cant_shows = int(input("\n¿Cuántos shows musicales ha visto en el último año?: "))
print("¿El usuario ha visto más de 3 shows? ", cant_shows > 3)

#### Problema 6
edad_cliente = int(input("\nIngrese la edad del cliente: "))
if edad_cliente < 4:
    print("Entrada gratis")
elif edad_cliente <= 18:
    print("El precio de la entrada es $5")
else:4
    print("El precio de la entrada es $10")

#### Problema 7
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nOperaciones:")
print("1. Suma\n2. Resta\n3. Multiplicación")
opcion_operacion = int(input("Elija una opción: "))

if opcion_operacion == 1:
    print("Resultado:", num1 + num2)
elif opcion_operacion == 2:
    print("Resultado:", num1 - num2)
elif opcion_operacion == 3:
    print("Resultado:", num1 * num2)
else:
    print("Opción inválida")

#### Problema 8
hora_ingresada = input("\nIngrese la hora en formato HH:MM: ")
hours, minutes = hora_ingresada.split(":")
time = int(hours) + int(minutes) / 60

if 7 <= time <= 8:
    print("Hora de desayunar")
elif 12 <= time <= 13:
    print("Hora de almorzar")
elif 18 <= time <= 19:
    print("Hora de cenar")
else:
    print("No es hora de comer")

#### Problema 9
cantidad_depositada = float(input("\nIngrese la cantidad depositada en la cuenta de ahorros: "))
for i in range(1, 4):
    cantidad_depositada = cantidad_depositada * 1.04
    print(f"Cantidad depositada en el año {i}: {cantidad_depositada:.2f}")

#### Problema 10
import math
print("\nIngrese la ecuación de segundo grado ax² + bx + c = 0")
a = float(input("\nIngrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Todos los números son solución")
        else:
            print("Ecuación no presenta solución real")
    else:
        print(f"Solución única: x = {-c / b}")
else:
    discriminante_ecuacion = b**2 - 4*a*c
    if discriminante_ecuacion < 0:
        print("Ecuación no presenta solución real")
    elif discriminante_ecuacion == 0:
        x = -b / (2*a)
        print(f"Solución única: x = {x}")
    else:
        x1 = (-b + math.sqrt(discriminante_ecuacion)) / (2*a)
        x2 = (-b - math.sqrt(discriminante_ecuacion)) / (2*a)
        print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")

