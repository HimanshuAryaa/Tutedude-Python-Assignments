# Assignment 7: Building Database Apps with PostgreSQL & Python

## Building Database Apps with PostgreSQL & Python

This assignment documents all practical exercises from Module 16, covering database fundamentals, PostgreSQL setup, and building database applications using Python.

---

## 📚 Lectures & Practicals Covered

### **Theory Lectures (1-4)**
1. Introduction to data
2. Introduction to database
3. Introduction to PostgreSQL
4. Installing PostgreSQL

### **PostgreSQL Practicals (5-8)**
5. Creating a database
6. Deleting a database
7. Creating table and adding data
8. Retrieving data from database and deleting contents in the table

### **Python Setup (9-10)**
9. Setting up virtualenv
10. Installing psycopg2

### **Python-PostgreSQL Integration (11-15)**
11. Connecting to the database
12. Creating table using python
13. Inserting the data using python
14. Extracting the data from the database
15. Adding the input from the user

---

## 🚀 Prerequisites

### Software Requirements
- **PostgreSQL** (version 12 or higher)
- **Python 3.x**
- **pgAdmin 4** (comes with PostgreSQL installation)
- **psycopg2** library

### Installation Commands
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install psycopg2
pip install psycopg2-binary
```

---

## 📂 Practical Exercises

### 🔹 Practical 5: Creating a Database
**Location**: `practical5_create_database/`

**What it covers:**
- Creating a new database in PostgreSQL
- Using pgAdmin or SQL commands

**Files:**
- `practical5_create_database.png` - Full screenshot showing database creation
- `sql_commands.txt` - SQL commands used and results

---

### 🔹 Practical 6: Deleting a Database
**Location**: `practical6_delete_database/`

**What it covers:**
- Deleting an existing database
- Understanding DROP DATABASE command

**Files:**
- `practical6_delete_database.png` - Full screenshot showing database deletion
- `sql_commands.txt` - SQL commands used and results

---

### 🔹 Practical 7: Creating Table and Adding Data
**Location**: `practical7_create_table_add_data/`

**What it covers:**
- Creating tables with proper data types
- Inserting data into tables
- Understanding PRIMARY KEY, data types

**Files:**
- `practical7_create_table_add_data.png` - Full screenshot showing table creation and data insertion
- `sql_commands.txt` - SQL commands used and results

---

### 🔹 Practical 8: Retrieving and Deleting Data
**Location**: `practical8_retrieve_delete_data/`

**What it covers:**
- SELECT queries to retrieve data
- DELETE statements to remove data
- Filtering with WHERE clause

**Files:**
- `practical8_retrieve_delete_data.png` - Full screenshot showing data retrieval and deletion
- `sql_commands.txt` - SQL commands used and results

---

### 🔹 Practical 9: Setting up Virtualenv
**Location**: `practical9_virtualenv_setup/`

**What it covers:**
- Creating Python virtual environment
- Activating virtual environment
- Understanding isolated Python environments

**Files:**
- `practical9_1_virtualenv_setup.png` - Full screenshot showing virtualenv setup
- `practical9_2_virtualenv_setup.png` - Full screenshot showing virtualenv setup
- `practical9_3_virtualenv_setup.png` - Full screenshot showing virtualenv setup

---

### 🔹 Practical 10: Installing psycopg2
**Location**: `practical10_install_psycopg2/`

**What it covers:**
- Installing psycopg2 library
- Verifying installation

**Files:**
- `practical10_1_install_psycopg2.png` - Full screenshot showing installation process
- `practical10_2_install_psycopg2.png` - Full screenshot showing installation process

---

### 🔹 Practical 11: Connecting to the Database
**Location**: `practical11_database_connection/`

**What it covers:**
- Establishing connection between Python and PostgreSQL
- Using connection parameters (host, database, user, password)
- Testing connection

**Files:**
- `practical11_database_connection.png` - Full screenshot showing successful connection
- `test.py` - Python code for database connection

---

### 🔹 Practical 12: Creating Table Using Python
**Location**: `practical12_create_table_python/`

**What it covers:**
- Executing CREATE TABLE statements from Python
- Using cursor objects
- Committing changes

**Files:**
- `practical12_1_create_table_python.png` - Full screenshot showing table creation
- `practical12_2_create_table_python.png` - Full screenshot showing table creation
- `test.py` - Python code for creating tables

---

### 🔹 Practical 13: Inserting Data Using Python
**Location**: `practical13_insert_data_python/`

**What it covers:**
- Executing INSERT statements from Python
- Using parameterized queries
- Preventing SQL injection

**Files:**
- `practical13_1_insert_data_python.png` - Full screenshot showing data insertion
- `practical13_2_insert_data_python.png` - Full screenshot showing data insertion
- `test.py` - Python code for inserting data

---

### 🔹 Practical 14: Extracting Data from Database
**Location**: `practical14_extract_data_python/`

**What it covers:**
- Executing SELECT queries from Python
- Fetching results (fetchone, fetchall, fetchmany)
- Processing query results

**Files:**
- `practical14_1_extract_data_python.png` - Full screenshot showing data extraction
- `practical14_2_extract_data_python.png` - Full screenshot showing data extraction
- `test.py` - Python code for retrieving data

---

### 🔹 Practical 15: Adding Input from User
**Location**: `practical15_user_input/`

**What it covers:**
- Taking user input for database operations
- Building interactive database applications
- Complete CRUD operations with user interaction

**Files:**
- `practical15_1_user_input.png` - Full screenshot showing user input functionality
- `practical15_2_user_input.png` - Full screenshot showing user input functionality
- `test.py` - Python code for user input handling

---

## 💡 Learning Objectives

- Understanding database fundamentals and terminology
- Installing and configuring PostgreSQL
- Writing SQL queries (CREATE, INSERT, SELECT, DELETE, DROP)
- Setting up Python virtual environments
- Connecting Python applications to PostgreSQL databases
- Executing SQL commands from Python code
- Using psycopg2 library effectively
- Building interactive database applications
- Understanding database security and best practices
- Implementing CRUD (Create, Read, Update, Delete) operations

---

## 🛠️ Database Schema Examples

### Sample Table Structure
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    course VARCHAR(50)
);
```

### Sample Data
```sql
INSERT INTO students (name, age, course) 
VALUES ('John Doe', 20, 'Python Programming');
```

---

## 🔧 Common Connection Parameters
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="postgres",
    password="your_password"
)
```

---

## 📁 Files

### Project Structure
```
assignment7/
├── README.md
├── practical5_create_database/
│   ├── practical5_create_database.png
│   └── sql_commands.txt
├── practical6_delete_database/
│   ├── practical6_delete_database.png
│   └── sql_commands.txt
├── practical7_create_table_add_data/
│   ├── practical7_create_table_add_data.png
│   └── sql_commands.txt
├── practical8_retrieve_delete_data/
│   ├── practical8_retrieve_delete_data.png
│   └── sql_commands.txt
├── practical9_virtualenv_setup/
│   ├── practical9_1_virtualenv_setup.png
│   ├── practical9_2_virtualenv_setup.png
│   └── practical9_3_virtualenv_setup.png
├── practical10_install_psycopg2/
│   ├── practical10_1_install_psycopg2.png
│   └── practical10_1_install_psycopg2.png
├── practical11_database_connection/
│   ├── practical11_database_connection.png
│   └── test.py
├── practical12_create_table_python/
│   ├── practical12_1_create_table_python.png
│   ├── practical12_2_create_table_python.png
│   └── test.py
├── practical13_insert_data_python/
│   ├── practical13_1_insert_data_python.png
│   ├── practical13_2_insert_data_python.png
│   └── test.py
├── practical14_extract_data_python/
│   ├── practical14_1_extract_data_python.png
│   ├── practical14_2_extract_data_python.png
│   └── test.py
└── practical15_user_input/
    ├── practical15_1_user_input.png
    ├── practical15_2_user_input.png
    └── test.py
```

### File List
- `README.md` - This documentation file
- `practical5_create_database/` - Database creation practical
- `practical6_delete_database/` - Database deletion practical
- `practical7_create_table_add_data/` - Table creation and data insertion
- `practical8_retrieve_delete_data/` - Data retrieval and deletion
- `practical9_virtualenv_setup/` - Virtual environment setup
- `practical10_install_psycopg2/` - psycopg2 installation
- `practical11_database_connection/` - Python-PostgreSQL connection
- `practical12_create_table_python/` - Creating tables via Python
- `practical13_insert_data_python/` - Inserting data via Python
- `practical14_extract_data_python/` - Extracting data via Python
- `practical15_user_input/` - User input integration

---

## 👤 Author

[Himansu Arya]
Created as part of the TuteDude Python Programming Course - Module 16

---

## 📄 License

This project is for educational purposes as part of the TuteDude Python course.
