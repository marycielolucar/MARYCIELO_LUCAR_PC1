def obtener_MIME(archivo_a_evaluar):
    extensiones_archivo = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    archivo_a_evaluar = archivo_a_evaluar.lower().strip()
    for ext, tipo in extensiones_archivo.items():
        if archivo_a_evaluar.endswith(ext):
            return tipo
    return "application/octet-stream"

print(obtener_MIME("happy.jpg"))
print(obtener_MIME("document.pdf"))
