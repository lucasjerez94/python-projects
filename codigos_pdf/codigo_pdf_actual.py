import os
import shutil
import pdfplumber
import re

# Carpeta donde se encuentran los archivos PDF originales
carpeta_origen = 'C:/Users/ljerez/Desktop/pruebapdf/originales' 
carpeta_destino = 'C:/Users/ljerez/Desktop/pruebapdf/modificados'

# Obtener una lista de todos los archivos PDF en la carpeta origen
archivos_pdf = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.pdf')]

# Iterar sobre los archivos PDF y copiarlos con el nuevo nombre y ruta
for archivo_pdf in archivos_pdf:
    ruta_original = os.path.join(carpeta_origen, archivo_pdf)
    
    # Abre el archivo PDF con pdfplumber
    with pdfplumber.open(ruta_original) as pdf:
        texto_pdf = ''
        for page in pdf.pages:
            texto_pdf += page.extract_text()
    
    # Realiza la lógica para obtener el nuevo nombre
    nombre_completo = None
    for line in texto_pdf.split('\n'):
        if "DNI" in line:
            nombre_completo = re.sub(r'\d', '', line.replace("DNI", "").strip())
            break
    
    if nombre_completo:
        nuevo_nombre = f"{nombre_completo.strip()} 2 do  .pdf"# Agrega "3 er" al nombre
    else:
        nuevo_nombre = f"{archivo_pdf} 2 do"  # Agrega "3 er" al nombre original si no se encuentra "DNI"
    
    # Elimina caracteres no permitidos en el nombre del archivo
    nuevo_nombre = ''.join(c for c in nuevo_nombre if c.isalnum() or c in ' -_.()[]')
    
    nueva_ruta = os.path.join(carpeta_destino, nuevo_nombre)

    # Copiar el archivo con el nuevo nombre y ruta
    shutil.copy(ruta_original, nueva_ruta)

    print(f'Archivo {archivo_pdf} copiado y renombrado a: {nuevo_nombre}')

    