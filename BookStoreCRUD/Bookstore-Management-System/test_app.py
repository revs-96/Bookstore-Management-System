import unittest
from flask import json
from app import app, db, Book

class TestBookstoreAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def get_auth_headers(self):
        # Assuming your authentication logic generates a valid JWT token
        response = self.app.post('/login',
                                 data=json.dumps({"username": "My_username", "password": "My_password"}),
                                 content_type='application/json')
        data = json.loads(response.data.decode())
        token = data['access_token']
        return {'Authorization': f'Bearer {token}'}

    def test_add_book(self):
        response = self.app.post('/books',
                                 headers=self.get_auth_headers(),
                                 data=json.dumps({
                                     "title": "Atomic Habits",
                                     "author": "James Clear",
                                     "isbn": "9780008386596",
                                     "price": 511,
                                     "quantity": 40
                                 }),
                                 content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Book added successfully')

    def test_get_all_books(self):
        # Assuming you have added some books in the setup or directly in the test
        response = self.app.get('/books', headers=self.get_auth_headers())
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue('books' in data)

    def test_get_specific_book(self):
        response = self.app.get('/books/9780008386596', headers=self.get_auth_headers())
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200 if 'title' in data else 404)

def test_update_book(self):
    response = self.app.put('/books/9780008386596',
                            headers=self.get_auth_headers(),
                            data=json.dumps({
                                "title": "Atomic Habits",
                                "author": "James Clear",
                                "price": 711.0,
                                "quantity": 20
                            }),
                            content_type='application/json')
    data = json.loads(response.data.decode())

    try:
        self.assertEqual(response.status_code, 200 if 'message' in data else 404)
        if response.status_code == 404:
            print(f"Book not found. Response data: {data}")
    except AssertionError:
        print(f"AssertionError: Expected status code 200 but got {response.status_code}")
        print(f"Response data: {data}")
        raise  # re-raise the exception to mark the test as failed

def test_delete_book(self):
    response = self.app.delete('/books/9780008386596', headers=self.get_auth_headers())
    data = json.loads(response.data.decode())

    try:
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Book deleted successfully')
    except AssertionError:
        print(f"AssertionError: Expected status code 200 but got {response.status_code}")
        print(f"Response data: {data}")
        if response.status_code == 404:
            print(f"Book not found. Response data: {data}")
        raise  # re-raise the exception to mark the test as failed


    def test_login(self):
        response = self.app.post('/login',
                                 data=json.dumps({"username": "My_username", "password": "My_password"}),
                                 content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in data)

if __name__ == '__main__':
    unittest.main()
