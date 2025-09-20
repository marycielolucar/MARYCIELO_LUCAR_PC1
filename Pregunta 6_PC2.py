alumnos_NOTAS = []
cant_alumnos = int(input("¿Cuántos alumnos desea ingresar?: "))
for _ in range(cant_alumnos):
    nombre_alumno = input("Nombre del alumno: ")
    notas_alumno = [int(input(f"Ingrese nota {_+1}: ")) for _ in range(3)]
    alumnos_NOTAS.append({"Alumno": nombre_alumno, "Notas": notas_alumno})
print(alumnos_NOTAS)