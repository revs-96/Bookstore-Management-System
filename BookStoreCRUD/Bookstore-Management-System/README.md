# Bookstore Management System API

## Introduction

The Bookstore Management System API is a web service that provides CRUD (Create, Read, Update, Delete) operations for managing books in a bookstore.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/) 
- [Flask](https://pypi.org/project/Flask/) 
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/) 
- [Postman](https://www.postman.com/) (for testing API endpoints)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/revs-96/Bookstore-Management-System.git
    cd Bookstore-Management-System
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py create_db
    ```
### API Documentation

View the API documentation using Postman::

- [Postman API Documentation](https://documenter.getpostman.com/view/27921547/2s9YypFNsD)

  
### Usage

To run the application, use the following command:


```bash
python app.py
```
```bash
python test_app.py
```

## Endpoints

### GET /books
Retrieve a list of all books.

**Endpoint:**
- [http://127.0.0.1:5000/books](http://127.0.0.1:5000/books)

### GET /books/{isbn}
Retrieve details of a specific book.

**Endpoint:**
- [http://127.0.0.1:5000/books/9780008386642](http://127.0.0.1:5000/books/9780008386642)

### POST /books
Add a new book.

**Endpoint:**
- [http://127.0.0.1:5000/books](http://127.0.0.1:5000/books)

### PUT /books/{isbn}
Update details of a specific book.

**Endpoint:**
- [http://127.0.0.1:5000/books/9780008386642](http://127.0.0.1:5000/books/9780008386642)

### DELETE /books/{isbn}
Delete a specific book.

## Token Generation

### POST /login
Generate a token for authentication.

**Endpoint:**
- [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

## Request Examples

### POST /books

```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "isbn": "9780008386596",
    "price": 19.99,
    "quantity": 50
}
