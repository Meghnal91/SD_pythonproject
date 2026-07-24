import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password = "Khushi@17",
        database = "singup_db"
    )