import csv
import psycopg2
from mm import insert_data, query_data, delete_data, update_data, enter_data, upload_csv

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port="5432")
cur = conn.cursor()




# enter_data()
#upload_csv('numbers.csv')
#enter_data()

delete_data(name='ERSULTAN')

query_data()