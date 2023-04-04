"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os
from datetime import date
path_to_employees = os.path.join('north_data','employees_data.csv')
path_to_customers = os.path.join('north_data','customers_data.csv')
path_to_orders =  os.path.join('north_data','orders_data.csv')
with psycopg2.connect(host='localhost',database='north',user='postgres',password='Persik012') as conn:
    with conn.cursor() as cur:

            with open(path_to_employees, 'r', encoding="UTF-8", newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')

                for row in reader:

                    thedate = date.fromisoformat(row['birth_date'])

                    cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s)',(row['first_name'],row['last_name'],row['title'],thedate,row['notes']))
            with open(path_to_customers,'r',encoding='UTF=8',newline='') as customers:
                reader_customers = csv.DictReader(customers,delimiter=',')
                for row in reader_customers:
                    cur.execute('INSERT INTO customers VALUES (%s,%s,%s)', (row['customer_id'],row['company_name'],row['contact_name']))
            with open(path_to_orders, 'r', encoding="UTF-8", newline='') as orders:
                reader_order = csv.DictReader(orders, delimiter=',')
                for row in reader_order:
                    thedate = date.fromisoformat(row['order_date'])
                    cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s)', (row['order_id'],row['customer_id'],row['employee_id'],thedate,row['ship_city']))



conn.close()


