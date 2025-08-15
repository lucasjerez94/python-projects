import os
import shutil
import pdfplumber
import re

# Definir rutas de carpetas
CARPETA_ORIGEN = '/Users/Giise/OneDrive/Escritorio/3ER EIO'
CARPETA_DESTINO = '/Users/Giise/OneDrive/Escritorio/Nombres cambiados/Tercer EIO - cambiados'

def obtener_archivos_pdf(carpeta):
    """Obtiene una lista de archivos PDF en una carpeta dada."""
    return [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.pdf')]

def extraer_texto_pdf(ruta_pdf):
    """Extrae todo el texto de un archivo PDF."""
    texto_pdf = ''
    with pdfplumber.open(ruta_pdf) as pdf:
        for page in pdf.pages:
            texto_pdf += page.extract_text() or ''
    return texto_pdf

def obtener_nombre_desde_texto(texto):
    """Extrae el nombre a partir del texto usando la palabra clave 'DNI'."""
    for line in texto.split('\n'):
        if "DNI" in line:
            return re.sub(r'\d', '', line.replace("DNI", "").strip())
    return None

def limpiar_nombre(nombre):
    """Elimina caracteres no permitidos en nombres de archivo."""
    return ''.join(c for c in nombre if c.isalnum() or c in ' -_.()[]')

def copiar_y_renombrar_pdf(archivo_pdf):
    """Copia y renombra un archivo PDF basado en su contenido."""
    ruta_original = os.path.join(CARPETA_ORIGEN, archivo_pdf)
    texto_pdf = extraer_texto_pdf(ruta_original)
    
    nombre_completo = obtener_nombre_desde_texto(texto_pdf)
    nuevo_nombre = f"{nombre_completo if nombre_completo else archivo_pdf} 3 ER.pdf"
    nuevo_nombre = limpiar_nombre(nuevo_nombre)
    nueva_ruta = os.path.join(CARPETA_DESTINO, nuevo_nombre)

    shutil.copy(ruta_original, nueva_ruta)
    print(f'Archivo {archivo_pdf} copiado y renombrado a: {nuevo_nombre}')

def procesar_archivos():
    """Función principal para procesar todos los archivos PDF."""
    archivos_pdf = obtener_archivos_pdf(CARPETA_ORIGEN)
    for archivo_pdf in archivos_pdf:
        copiar_y_renombrar_pdf(archivo_pdf)

# Ejecutar el proceso principal
if __name__ == "__main__":
    procesar_archivos()
