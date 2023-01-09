import csv
import psycopg2


conn = psycopg2.connect(database='north',user='postgres', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            with open(r'customers_data.csv', 'r') as f:
                cur.copy_from(f, "customers", sep=',', null="")
            with open('employees_data.csv', 'r') as file:
                reader = csv.reader(file, delimiter='\t')
                new = []
                for row in reader:
                    a = row[0].replace('"', '')
                    b = a.split(',')
                    new.append(b)
                for i in range(len(new)):
                    cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)',
                            (i+1, new[i][0], new[i][1], new[i][2], new[i][3], new[i][4]))

            with open(r'orders_data.csv', 'r') as f:
                cur.copy_from(f, "orders", sep=',', null="")
finally:
    conn.close()