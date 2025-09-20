meses_fecha = {
    "Enero": 1, "Febrero": 2, 
    "Marzo": 3, "Abril": 4, 
    "Mayo": 5, "Junio": 6, 
    "Julio": 7, "Agosto": 8, 
    "Septiembre": 9, "Octubre": 10, 
    "Noviembre": 11, "Diciembre": 12
}

fecha_evaluar = input("Ingrese fecha (MM/DD/AAAA o 'Mes D, AAAA'): ").strip()
if "/" in fecha_evaluar:
    mes_entrada, dia_entrada, anho_entrada = fecha_evaluar.split("/")
    print(f"{int(anho_entrada):04}-{int(mes_entrada):02}-{int(dia_entrada):02}")
else:
    mes_entrada, resto = fecha_evaluar.split(" ", 1)
    dia_entrada, anho_entrada = resto.replace(",", "").split()
    print(f"{int(anho_entrada):04}-{meses_fecha[mes_entrada]:02}-{int(dia_entrada):02}")