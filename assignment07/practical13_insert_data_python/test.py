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
    cursor.execute('''insert into employees(Name,Id,Salary,Age) values('Anshu',01,90000,25);''')

    print('Data added successfully')

    conn.commit()
    conn.close()
data()
