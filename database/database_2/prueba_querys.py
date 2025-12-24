"""
from orders_repository import insert_order, get_all_orders

orders = get_all_orders()

for order in orders:
    print(order)
"""
from orders_repository import *

# create_test_table() Ya fue realizado, corroborado en MySQL Worbench

#Realizado insert_test(("Lucas Jerez", "lucas.jerez@mail.com", "2024-01-15"))
#Realizado insert_test(("Ana Pérez", "ana.perez@mail.com", "2024-03-22"))
#Realizado insert_test(("Martín Gómez", "martin.gomez@mail.com", "2024-06-10"))
#Realizado insert_test(("Sofía Rodríguez", "sofia.rodriguez@mail.com", "2024-09-05"))
#Realizado insert_test(("Juan López", "juan.lopez@mail.com", "2025-02-18"))

clientes = [
    ("María González", "maria.gonzalez@mail.com", "2023-11-08"),
    ("Pablo Fernández", "pablo.fernandez@mail.com", "2024-02-14"),
    ("Carolina Méndez", "carolina.mendez@mail.com", "2024-05-30"),
    ("Diego Ramírez", "diego.ramirez@mail.com", "2024-08-19"),
    ("Valentina Torres", "valentina.torres@mail.com", "2025-01-03"),
]

for cliente in clientes:
    insert_test(cliente)


