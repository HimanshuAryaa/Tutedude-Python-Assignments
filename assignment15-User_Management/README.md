# Assignment 15: User Profile Management API

## REST API's Using Django

A complete RESTful API built using Django REST Framework for managing user profiles with authentication, custom permissions, and CRUD operations on user data.

---

## 📌 Project Overview

### Description
A fully functional REST API application that handles user profile management using Django's built-in User model. The API includes user registration, profile retrieval, updating, deletion with authentication and custom permissions ensuring users can only modify their own profiles.

### Features
- ✨ User registration and listing
- 🔐 User authentication and authorization
- 🛡️ Custom permissions (users can only modify their own profiles)
- 👤 Individual profile retrieval and management
- 📝 Complete CRUD operations on user profiles
- ⚡ Django Admin integration for managing users
- 🔒 Secure profile update and deletion

---

## 📂 Project Structure
```
assignment15-User_Management/
├── user_project/
│   ├── user_project/
│       ├── __init__.py
│       ├── settings.py              # Django settings with REST framework config
│       ├── urls.py                  # Main URL configuration
│       ├── wsgi.py
│       └── asgi.py
│   ├── users/
│       ├── __init__.py
│       ├── models.py                # Uses Django's built-in User model
│       ├── views.py                 # API views with generics
│       ├── serializers.py           # User data serializers
│       ├── permissions.py           # Custom permission classes
│       ├── urls.py                  # App URL configuration
│       ├── admin.py                 # Admin panel configuration
│       ├── apps.py
│       ├── tests.py
│       └── migrations/
│            └── __init__.py
│   ├── db.sqlite3                   # SQLite database
│   ├── manage.py                    # Django management script
├── README.md                    # This documentation file
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed
- Django and Django REST Framework

### Installation Steps

1. **Install required packages**:
```bash
pip install django
pip install djangorestframework
```

2. **Apply migrations**:
```bash
python manage.py migrate
```

3. **Create a superuser** (for admin access):
```bash
python manage.py createsuperuser
```

4. **Run the development server**:
```bash
python manage.py runserver
```

5. **Access the API**:
```
User List/Registration: http://127.0.0.1:8000/api/profiles/
Specific User Profile: http://127.0.0.1:8000/api/profiles/{id}/
Admin Panel: http://127.0.0.1:8000/admin/
API Auth Login: http://127.0.0.1:8000/api-auth/login/
```

---

## 💻 API Endpoints

| Endpoint | Method | Description | Authentication Required |
|----------|--------|-------------|------------------------|
| `/api/profiles/` | GET | List all registered users | No |
| `/api/profiles/` | POST | Register a new user | No |
| `/api/profiles/{id}/` | GET | Retrieve a specific user profile | Yes |
| `/api/profiles/{id}/` | PUT | Update a user profile | Yes (Owner only) |
| `/api/profiles/{id}/` | PATCH | Partially update a profile | Yes (Owner only) |
| `/api/profiles/{id}/` | DELETE | Delete a user profile | Yes (Owner only) |

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 6.0.2** - Web framework
- **Django REST Framework** - RESTful API toolkit
- **SQLite** - Database (default)

---

## 🔧 Key Components

### Models
- **Django User Model**
  - Uses Django's built-in `User` model
  - Fields: `username`, `email`, `password`, `first_name`, `last_name`
  - No custom model needed

### Serializers (serializers.py)
- **UserSerializer**
  - Serializes User model data
  - Converts database models to JSON format
  - Handles user registration data

### Views (views.py)
- **UserListCreateAPIView** - ListCreateAPIView
  - Lists all registered users (GET)
  - Creates new user registration (POST)
  
- **UserRetrieveUpdateDestroyAPIView** - RetrieveUpdateDestroyAPIView
  - Retrieves specific user details (GET)
  - Updates user profile (PUT/PATCH)
  - Deletes user profile (DELETE)
  - Custom permissions applied

### Permissions (permissions.py)
- **IsOwnerOrReadOnly** - Custom permission class
  - Allows read access to all users
  - Restricts write/update/delete to profile owner only
  - Ensures security for profile management

### URL Configuration (urls.py)
- User list and registration endpoint
- Individual user profile endpoint with ID parameter
- Admin panel route
- API authentication routes

---

## 🔑 Key Concepts Implemented

### Django REST Framework Fundamentals
- Generic API Views (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
- Serializers for data transformation
- Custom permissions for security
- Authentication and authorization

### API Design
- RESTful endpoint structure
- Proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Custom permission classes for owner-only access
- Using generics for better endpoint control

### Security
- Authentication required for modifications
- Object-level permissions
- Owner-only update and delete
- CSRF protection

---

## 💡 Learning Objectives

- Building RESTful APIs with Django REST Framework
- Using generic API views for cleaner code
- Implementing custom permission classes
- Working with Django's built-in User model
- User authentication and authorization
- Creating serializers for data conversion
- Understanding CRUD operations via API
- Using Django admin for user management
- Endpoint design and URL routing

---

## 📁 Files

- `userprofile/settings.py` - Django settings with REST framework configuration
- `userprofile/urls.py` - Main URL routing configuration
- `users/views.py` - API views using generics
- `users/serializers.py` - UserSerializer for API responses
- `users/permissions.py` - IsOwnerOrReadOnly custom permission
- `users/urls.py` - App-specific URL configuration
- `users/admin.py` - Admin panel configuration
- `README.md` - This documentation file

---

## 📦 Requirements.txt
```
Django==6.0.2
djangorestframework==3.14.0
```

---

## 👤 Author

Himanshu Arya  
Created as part of the TuteDude Python Programming Course

---

## 📄 License

This project is for educational purposes as part of the TuteDude Python course.