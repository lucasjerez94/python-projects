def calcular_interes_compuesto(monto, tasa, años):
    interes_compuesto = monto * (1 + tasa/100)**años
    return interes_compuesto

monto = float(input("Ingrese el monto inicial: "))
tasa = float(input("Ingrese la tasa de interés (en porcentaje): "))
años = int(input("Ingrese el número de años: "))

resultado = calcular_interes_compuesto(monto, tasa, años)
print("El monto final después de", años, "años es:", resultado)
