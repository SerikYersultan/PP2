import csv
import psycopg2
from phone import insert_data, query_data, delete_data, update_data, enter_data, upload_csv
from phone import get_records_by_pattern, insert_or_update_user, insert_many_users, query_data_with_pagination, delete_data_by_username_or_phone


conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()



userlist = [
    ("No", "No", "7017017012"), 
    ("New", "User", "0987654721"),
    ("User", "Neww", "1431231234"),
    ("Hello", "World", "3213993214")
]

# insert_many_users(userlist)

# get_records_by_pattern("Te")
# insert_or_update_user("New", "User", "12345678")

# update_data(id=10, first_name="Updatedname")

insert_many_users(userlist)

# upload_csv("./numbers.csv")
query_data()