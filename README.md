# CRM Application with Django Rest Framework

## Overview

This is a CRM (Customer Relationship Management) application built using Django Rest Framework. The application provides a basic example of how to implement CRUD operations and user authentication.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete records.
- **User Authentication**: User login and authentication functionality.
- **RESTful API Endpoints**: Exposes API endpoints for the CRM functionality.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 4.0 or higher
- Django Rest Framework 3.14 or higher

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/CRMApplication.git
   cd CRMApplication

2. **Create a Virtual Environment**

    python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate

3. **Install Dependencies**

    pip install -r requirements.txt

4. **Apply Migrations**

    python manage.py migrate

5. **Run the Development Server**

    python manage.py runserver