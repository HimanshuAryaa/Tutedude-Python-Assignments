# Tutedude-Python-Assignments

This repository contains all my assignment solutions from the TuteDude Python Programming course.

## 📚 Course Information
- **Course**: Python Programming
- **Platform**: TuteDude
- **Topics Covered**: Python Basics, OOP, File Handling, GUI Development, Database Apps, Data Analysis, Web Development (Flask & Django), Web Scraping, Computer Vision, Automation and more

## 📁 Repository Structure
```
Tutedude-Python-Assignments/
├── README.md
├── assignment1/
│   ├── README.md
│   ├── task1.py
│   └── task2.py
├── assignment2/
│   ├── README.md
│   ├── task1.py
│   └── task2.py
├── assignment3/
│   ├── README.md
│   ├── task1.py
│   └── task2.py
├── assignment4/
│   ├── README.md
│   ├── task1.py
│   ├── task2.py
│   ├── sample.txt (for Task 1) 
│   └── output.txt (for Task 2)
├── assignment5/
│   ├── README.md
│   ├── task1.py
│   └── task2.py
└──assignment6-tkinter-calculator/
│   ├── README.md
│   ├── src
│      └── calculator.py                     - Main Tkinter application
│   └── screenshots/
│      ├── calculator_initial.png            - default state with 0
│      ├── calculator_operation.png          - showing 55
│      └── calculator_error.png              - division by zero error
└── assignment7/
│   ├── README.md
│   ├── practical5_create_database/          - Database creation practical
│   ├── practical6_delete_database/          - Database deletion practical
│   ├── practical7_create_table_add_data/    - Table creation and data insertion
│   ├── practical8_retrieve_delete_data/     - Data retrieval and deletion
│   ├── practical9_virtualenv_setup/         - Virtual environment setup
│   ├── practical10_install_psycopg2/        - psycopg2 installation
│   ├── practical11_database_connection/     - Python-PostgreSQL connection
│   ├── practical12_create_table_python/     - Creating tables via Python
│   ├── practical13_insert_data_python/      - Inserting data via Python
│   ├── practical14_extract_data_python/     - Extracting data via Python
│   └── practical15_user_input/              - User input integration
└── assignment8-Flask_Registration_Form/
│   ├── README.md
│   ├── registration_form.py                - Main Flask application
│   ├── templates/
│       ├── base.html                       - Base template with navbar and Bootstrap
│       ├── index.html                      - Registration form page
│       └── confirmation.html               - Success confirmation page
│   └── screenshots/
│       ├── registration_form.png           - Registration Form Screenshot
│       └── confirmation_page.png           - Confirmation Page Screenshot
└── (more assignments to come...)
└── assignment9-REST_API_Using_Django/
│   ├── blog/
│       ├── blog/
│           ├── __init__.py
│           ├── settings.py                 - Django settings with REST framework config
│           ├── urls.py                     - Main URL configuration
│           ├── wsgi.py
│           └── asgi.py
│       ├── restapp/
│           ├── __init__.py
│           ├── models.py                   - BlogPost model
│           ├── views.py                    - API views and viewsets
│           ├── serializers.py              - Data serializers
│           ├── permissions.py              - Custom permission classes
│           ├── filters.py                  - Custom filter classes
│           ├── admin.py                    - Admin panel configuration
│           ├── apps.py
│           ├── tests.py
│           └── migrations/
│       ├── db.sqlite3                      - SQLite database
│       ├── manage.py                       - Django management script
│       ├── screenshots/
│           ├── api_hello_world.png
│           ├── post_list.png
│           ├── post_create.png
│           ├── post_detail.png
│           ├── post_filter.png
│           ├── post_search.png
│           └── admin_panel.png
│       └── README.md                       - This documentation file
├── assignment10-Price_Tracker/
│   ├── README.md                           - This documentation file
│   ├── price_tracker.py                    - Main web scraping application
│   ├── Scraper/                            - Auto-generated folder for output
│   │   ├── prices.csv                      - CSV file with product data
│   │   └── *.jpg                           - Downloaded product images
│   └── screenshots/
│       ├── csv_output.png
│       ├── downloaded_image.png
│       └── scraped_data.png
└── (more assignments to come...)
```

## 📝 Assignments

### [Assignment 1: Basic Python Concepts](./assignment1/)
**Basic Python Concepts**
- **Task 1**: Perform Basic Mathematical Operations
- **Task 2**: Create a Personalized Greeting

### [Assignment 2: Control Structures in Python](./assignment2/)
**Control Structures in Python**
- **Task 1**: Check if a Number is Even or Odd
- **Task 2**: Sum of Integers from 1 to 50 Using a Loop

### [Assignment 3: Functions & Modules in Python](./assignment3/)
**Functions & Modules in Python**
- **Task 1**: Calculate Factorial Using a Function
- **Task 2**: Using the Math Module for Calculations

### [Assignment 4: Files, Exceptions, and Errors in Python](./assignment4/)
**Files, Exceptions, and Errors in Python**
- **Task 1**: Read a File and Handle Errors
- **Task 2**: Write and Append Data to a File

### [Assignment 5: Data Structures and Strings in Python](./assignment5/)
**Data Structures and Strings in Python**
- **Task 1**: Create a Dictionary of Student Marks
- **Task 2**: Demonstrate List Slicing

### [Assignment 6: Calculator Using Tkinter](./assignment6-tkinter-calculator/)
**Calculator Using Tkinter**
- GUI-based calculator application with basic arithmetic operations
- Built with Python Tkinter library

### [Assignment 7: Building Database Apps with PostgreSQL & Python](./assignment7/)
**Building Database Apps with PostgreSQL & Python**
- Complete documentation of all 15 lectures and practicals
- PostgreSQL database operations
- Python-PostgreSQL integration using psycopg2
- Includes 11 practical exercises with screenshots and code

### [Assignment 8: Flask Registration Form Project](./assignment8-Flask_Registration_Form/)
**Flask - Registration Form Project**
- Full-stack web application with user registration form
- Built with Flask framework and Bootstrap 5
- Real-time password validation with JavaScript
- Template inheritance and responsive design

### [Assignment 9: REST API Using Django](./assignment9-REST_API_Using_Django/)
**REST API's Using Django**
- Complete RESTful API for blog post management
- User authentication and custom permissions
- Advanced filtering, searching, and pagination
- Built with Django REST Framework

### [Assignment 10: Web Scraping Implementation](./assignment10-Price_Tracker/)
**Web Scraping Module Implementation**
- Amazon price tracker application
- Product data scraping (title, price, image)
- CSV data storage for price history
- Automatic image downloading
- Built with BeautifulSoup and requests

## 🚀 How to Use This Repository

1. Navigate to the specific assignment folder
2. Read the assignment's README.md for details
3. Run files based on the project type:

**For Basic Python (Assignments 1-5):**
```bash
python task1.py
python task2.py
```

**For Tkinter project (Assignment 6):**
```bash
python calculator.py
```

**For Flask project (Assignment 8):**
```bash
pip install flask
python registration_form.py
```

## 🛠️ Requirements

- **Python 3.x**
- **Tkinter** - Built-in with Python (Assignment 6)
- **PostgreSQL** - Database server (Assignment 7)
- **psycopg2-binary** - PostgreSQL adapter for Python (Assignment 7)
- **Flask** - Web framework (Assignment 8)

## 👤 Author
Himanshu Arya

## 📄 License
This repository is for educational purposes as part of the TuteDude Python course.

---

*Last Updated: February 2026*
