# Book Management System

This is a Django-based web application for managing books and publishers. It allows users to add, update, delete, and view information about books and their respective publishers.

## Features

- Manage book records (title, authors, publisher, published date, ISBN, etc.)
- Manage publisher records
- Manage Authors
- Manage Genre


## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [Usage](#usage)
- [License](#license)

## Requirements

- Python 3.x
- Django 5.x
- pip (Python package installer)

## Installation

    Follow the steps below to set up the project on your local machine.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/book-management-system.git

    Replace your username with your GitHub username.

2. **Navigate into the project directory:**

    ```bash
    cd book-management-system


4. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv or python3 -m venv venv

5. **Activate the virtual environment:**

    On Windows:

    ```bash
    venv\Scripts\activate

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    
6. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt



## Installation


1. **Apply migrations:**

    Run the following command to set up the database schema:

    ```bash
    python manage.py migrate

2. **Create a superuser (optional):**

    If you want to access the Django admin interface, create a superuser account:

    ```bash
    python manage.py createsuperuser

## Running the Server

    To start the development server, run the following command:

    ```bash
    python manage.py runserver

    Now, open your web browser and navigate to http://127.0.0.1:8000/ to access the application.



