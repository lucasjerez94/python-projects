from datetime import datetime

#Explicacion del *args , **kwargs
"""
def mostrarDatos(*args, **kwargs):
    print("args: ",args)
    print("kwargs: ",kwargs)

mostrarDatos("Lucas", 35, pais = "Argentina", rol = "Analista", añosExperiencia = 5)
"""
#Explicación del {func.__name}
"""
def saludar():
    pass
print(f'El nombre de la funcion es:{saludar.__name__}')
"""

ahora = datetime.now()
print(ahora)

hora_formateada = ahora.strftime('%H:%M:%S')

