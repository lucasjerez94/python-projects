import os
from collections import defaultdict

def encontrar_archivos_duplicados(ruta):
    archivos_duplicados = defaultdict(list)
    for directorio_raiz, directorios, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_completa = os.path.join(directorio_raiz, archivo)
            tamaño = os.path.getsize(ruta_completa)
            archivos_duplicados[(archivo, tamaño)].append(ruta_completa)

    for clave, valor in archivos_duplicados.items():
        if len(valor) > 1:
            print(f"Archivos duplicados de '{clave[0]}' (tamaño {clave[1]} bytes):")
            for archivo in valor:
                print(f"- {archivo}")

ruta = input("Ingrese la ruta del directorio a buscar: ")
encontrar_archivos_duplicados(ruta)
