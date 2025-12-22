from db_connection import get_connection

# CREATE
def create_orders_table():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        customer_name VARCHAR(30) NOT NULL,
        product_name VARCHAR(20) NOT NULL,
        date_ordered DATE,
        quantity INT,
        unit_price FLOAT,
        phone_number VARCHAR(20)
    );
    """
    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()

# INSERT
def insert_order(order):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO orders (
        order_id, customer_name, product_name,
        date_ordered, quantity, unit_price, phone_number
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, order)
    connection.commit()

    cursor.close()
    connection.close()


# SELECT
def get_all_orders():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return results


# UPDATE
def update_price(order_id, new_price):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE orders SET unit_price = %s WHERE order_id = %s"
    cursor.execute(query, (new_price, order_id))

    connection.commit()
    cursor.close()
    connection.close()


# DELETE
def delete_order(order_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM orders WHERE order_id = %s"
    cursor.execute(query, (order_id,))

    connection.commit()
    cursor.close()
    connection.close()


