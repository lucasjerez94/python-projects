import os
import shutil
import pdfplumber
import re
from datetime import datetime

# ==============================
# DECORADOR PARA LOGS
# ==============================
def log_proceso(func):
    """Decorador que muestra cuándo inicia y finaliza una función."""
    def wrapper(*args, **kwargs):
        print(f"\n--> Iniciando: {func.__name__}() a las {datetime.now().strftime('%H:%M:%S')}")
        resultado = func(*args, **kwargs)
        print(f"<-- Finalizó: {func.__name__}() correctamente.\n")
        return resultado
    return wrapper


# ==============================
# CLASE LECTORA DE PDF (Inyección de dependencia)
# ==============================
class PDFReader:
    """Encargada de extraer texto de un PDF usando pdfplumber."""
    def leer_texto(self, ruta_pdf):
        with pdfplumber.open(ruta_pdf) as pdf:
            return ''.join(page.extract_text() for page in pdf.pages if page.extract_text())


# ==============================
# CLASE PRINCIPAL PARA RENOMBRAR PDFs
# ==============================
class PDFRenamer:
    def __init__(self, carpeta_origen, carpeta_destino, lector_pdf):
        self.carpeta_origen = carpeta_origen
        self.carpeta_destino = carpeta_destino
        self.lector_pdf = lector_pdf

    def extraer_nombre(self, texto):
        """Busca la línea que contiene 'DNI' y obtiene el nombre."""
        for line in texto.split('\n'):
            if "DNI" in line:
                return re.sub(r'\d', '', line.replace("DNI", "").strip())
        return None

    def limpiar_nombre(self, nombre):
        """Elimina caracteres no permitidos en nombres de archivos."""
        return ''.join(c for c in nombre if c.isalnum() or c in ' -_.()[]')

    @log_proceso
    def procesar_archivos(self):
        """Procesa todos los archivos PDF en la carpeta origen."""
        archivos_pdf = [
            archivo for archivo in os.listdir(self.carpeta_origen)
            if archivo.lower().endswith('.pdf')
        ]

        if not archivos_pdf:
            print("No se encontraron archivos PDF en la carpeta origen.")
            return

        for archivo in archivos_pdf:
            ruta_original = os.path.join(self.carpeta_origen, archivo)
            texto = self.lector_pdf.leer_texto(ruta_original)
            nombre = self.extraer_nombre(texto)

            if nombre:
                nuevo_nombre = f"{nombre.strip()} 3 er.pdf"
            else:
                nuevo_nombre = f"{os.path.splitext(archivo)[0]} 3 er.pdf"

            nuevo_nombre = self.limpiar_nombre(nuevo_nombre)
            nueva_ruta = os.path.join(self.carpeta_destino, nuevo_nombre)

            shutil.copy(ruta_original, nueva_ruta)
            print(f"✅ Archivo '{archivo}' copiado y renombrado a: '{nuevo_nombre}'")


# ==============================
# BLOQUE PRINCIPAL
# ==============================
if __name__ == "__main__":
    # RUTAS - modificá según tus carpetas
    carpeta_origen = r"/Users/Giise/OneDrive/Imágenes/Escritorio/3"
    carpeta_destino = r"/Users/Giise/OneDrive/Imágenes/Escritorio/3"

    lector_pdf = PDFReader()
    renamer = PDFRenamer(carpeta_origen, carpeta_destino, lector_pdf)
    renamer.procesar_archivos()
