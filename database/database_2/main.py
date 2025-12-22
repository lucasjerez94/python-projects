from orders_repository import *

create_orders_table()

insert_order((201, "Lucas", "Keyboard", "2025-09-18", 1, 120, "111111111"))

orders = get_all_orders()
for order in orders:
    print(order)

update_price(201, 150)
delete_order(201)


