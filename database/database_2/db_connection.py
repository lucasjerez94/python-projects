import pymysql
from db_config import DB_CONFIG

def get_connection():
    """
    Crea y devuelve una conexión a MySQL
    """
    return pymysql.connect(**DB_CONFIG)
