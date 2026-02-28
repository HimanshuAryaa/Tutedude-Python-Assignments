import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='123@123', host='localhost', port='5432')

cursor = conn.cursor()
cursor.execute('''create table employees(Name text, Id int, Salary int, Age int);''')

print('Table Created Successfully')

conn.commit()
conn.close()
