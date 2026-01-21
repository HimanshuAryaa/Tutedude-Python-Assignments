import psycopg2
def table():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123@123', host='localhost', port='5432')

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name text, Id int, Salary int, Age int);''')

    print('Table Created Successfully')

    conn.commit()
    conn.close()
def data():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='123@123', host='localhost', port='5432')

    cursor = conn.cursor()

    name = input("Enter Name: ")
    id = input("Enter ID: ")
    salary = input("Enter Salary: ")
    age = input("Enter Age: ")

    query = '''insert into employees(Name,Id,Salary,Age) values(%s,%s,%s,%s);'''
    cursor.execute(query,(name,id,salary,age))

    print('Data added successfully')

    conn.commit()
    conn.close()
data()
