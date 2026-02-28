# Assignment 16: Flask Registration Form with Database

## Flask - Registration Form with Database Integration

A complete web-based registration form application built using Flask framework with form validation, database storage, and secure password handling.

---

## 📌 Project Overview

### Description
A fully functional registration form web application that allows users to register with their details and stores the data in a SQLite database. The application includes Flask-WTF form validation, email validation, password confirmation checking, and secure database integration with SQLAlchemy.

### Features
- ✨ User registration form with validation
- 🗄️ Database storage using SQLAlchemy
- 📧 Email format validation
- 🔒 Password confirmation matching
- ⚠️ Form error display for user feedback
- 🛡️ CSRF protection with Flask-WTF
- 💾 Automatic database table creation
- 🎨 Clean and responsive UI
- ✅ Server-side form validation

---

## 📂 Project Structure
```
assignment16-Flask_Registration_Form_Database/
├── app.py                         # Main Flask application
├── forms.py                       
├── models.py                       
├── templates/
│   ├── base.html                 # Base Template for all pages
│   ├── index.html                # Registration form page
│   └── success.html              # Success confirmation page
├── instance/
│   └── site.db                  # SQLite database (auto-generated)
└── README.md                     # This documentation file
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed
- Flask and required extensions

### Installation Steps

1. **Install required packages**:
```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install email-validator
```

2. **Run the application**:
```bash
python app.py
```

3. **Open in browser**:
```
http://127.0.0.1:5000
```

4. **Database creation**:
- Database table is created automatically on first run
- Located at `instance/site.db`

---

## 💻 How It Works

1. **Registration Form**: User fills in name, email, password, and confirm password
2. **Form Validation**: Flask-WTF validates all fields (email format, password match)
3. **Error Display**: If validation fails, specific error messages are shown
4. **Database Storage**: Valid data is saved to SQLite database
5. **Success Page**: User sees confirmation after successful registration

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **Flask-WTF** - Form handling and validation
- **email-validator** - Email validation library
- **SQLite** - Database
- **Jinja2** - Template engine
- **HTML5** - Page structure
- **CSS3** - Styling

---

## 🔧 Key Components

### Database Model (app.py)
- **User Model**
  - `id` - Integer, Primary Key
  - `name` - String, required
  - `email` - String, unique, required
  - `password` - String, required

### Form Class (app.py)
- **RegistrationForm (FlaskForm)**
  - `name` - StringField with validators
  - `email` - EmailField with email validator
  - `password` - PasswordField with validators
  - `confirm_password` - PasswordField with EqualTo validator
  - `submit` - SubmitField

### Application Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET, POST | Registration form page |
| `/success` | GET | Success confirmation page |

---

## 🔑 Key Concepts Implemented

### Flask Fundamentals
- Flask application setup with SQLAlchemy
- Route creation with multiple HTTP methods
- Form handling with Flask-WTF
- Database integration with Flask-SQLAlchemy
- Application context for database operations
- Secret key configuration for CSRF protection

### Form Validation
- Email format validation with email-validator
- Password confirmation matching with EqualTo
- Required field validation
- Error message display in templates
- Form error loop in HTML

### Database Operations
- Model definition with SQLAlchemy
- Automatic table creation with `db.create_all()`
- Database session management
- Adding and committing data
- Using `with app.app_context()` for database operations

### Security
- CSRF protection with Flask-WTF
- Password storage (can be enhanced with hashing)
- Email uniqueness constraint
- Form validation before database insertion

---

## 💡 Learning Objectives

- Building web forms with Flask-WTF
- Form validation with validators
- Integrating SQLAlchemy with Flask
- Database model creation and migrations
- Handling form submissions
- Displaying validation errors to users
- CSRF protection implementation
- Email validation with external library
- Application context management
- Database CRUD operations

---

## 🔮 Possible Enhancements

Future improvements that could be added:
- Password hashing with `bcrypt` or `werkzeug.security`
- Login/logout functionality
- User dashboard
- Email verification
- Password reset feature
- Profile update functionality
- Session-based authentication
- Remember me functionality

---

## 👤 Author

[Himanshu Arya]  
Created as part of the TuteDude Python Programming Course

---

## 📄 License

This project is for educational purposes as part of the TuteDude Python course.