# AutoMax Car-Rental System

AutoMax is a comprehensive car rental system built with Django. It provides functionalities for managing car rentals, including user authentication, car listings, booking management, and more.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Setup

1. **Clone the repository:**

   ```
    git clone https://github.com/yourusername/automax.git
    cd automax
   ```
2. **Create and activate a virtual environment:**
    ```
        # On Windows
        python -m venv env
        .\env\Scripts\activate

        # On macOS and Linux
        python3 -m venv env
        source env/bin/activate
    ```

3. **Install the dependencies:**
    ```
    pip install -r requirements.txt

    ```

4. **Set up the database:**
    ```
    python manage.py migrate

    ```

5. **Create a superuser:**
    ```
    python manage.py createsuperuser
    ```

6. **Collect Staticfiles**

    ```
    python manage.py collectstatic
    ```



* Features
    - User Authentication
    - Sign Up
    - Login
    - Logout
* Car Listings
    - View Available Cars
    - Search Cars
* Booking Management
    - Book a Car
    - View Bookings
    - Cancel Booking
* Admin Panel
    - Manage Users
    - Manage Car Listings
    - View Bookings




8. **Project Structure**
    ```
    automax/
    ├── automax/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── car_rental/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   └── static/
    ├── manage.py
    ├── requirements.txt
    └── .env
    ```