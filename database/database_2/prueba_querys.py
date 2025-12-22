from orders_repository import insert_order, get_all_orders

orders = get_all_orders()

for order in orders:
    print(order)
    
