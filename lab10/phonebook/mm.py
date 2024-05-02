import csv
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")

conn.commit()

def insert_data(first_name, last_name, phone):
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            name, lastname, phone = row[0].split(';')
            insert_data(name, lastname, phone)

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def update_data(id, first_name=None, phone=None):
    if first_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE id = %s", (first_name, id))
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
    conn.commit()

def query_data(filter=None):
    if filter:
        cur.execute("SELECT * FROM phonebook WHERE %s", (filter,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()




upload_csv(r'C:\pp2\lab10\phonebook\numbers.csv')
#enter_data()  # Запустите эту функцию, чтобы ввести данные вручную через консоль.
#upload_csv(r'C:\pp2\lab10\phonebook\numbers.csv')  # Замените 'path_to_your_file.csv' на путь к вашему файлу.
#update_data(id=1, first_name="Иван", phone="1234567890")  # Обновите данные для записи с id=1.
#query_data()  # Показать все данные в таблице.query_data("first_name = 'Иван'")  # Показать данные для Ивана.
#delete_data(name="Иван")  # Удалить запись по имени.delete_data(phone="1234567890")  # Удалить запись по телефону.

