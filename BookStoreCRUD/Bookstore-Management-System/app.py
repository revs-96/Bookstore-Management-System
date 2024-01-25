from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret key
db = SQLAlchemy(app)
jwt = JWTManager(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Add your authentication logic here (e.g., check username and password against a database)
    if username == 'root' and password == 'root':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401


@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], isbn=data['isbn'], price=data['price'],
                    quantity=data['quantity'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 200


@app.route('/books', methods=['GET'])
@jwt_required()
def get_all_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_list.append({
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price,
            'quantity': book.quantity
        })
    return jsonify({"books": book_list}), 200


@app.route('/books/<isbn>', methods=['GET'])
@jwt_required()
def get_specific_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        return jsonify({
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price,
            'quantity': book.quantity
        }), 200
    else:
        return jsonify({"message": "Book not found"}), 404


@app.route('/books/<isbn>', methods=['PUT'])
@jwt_required()
def update_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        data = request.get_json()
        book.title = data['title']
        book.author = data['author']
        book.price = data['price']
        book.quantity = data['quantity']
        db.session.commit()
        return jsonify({"message": "Book updated successfully"}), 200
    else:
        return jsonify({"message": "Book not found"}), 404


@app.route('/books/<isbn>', methods=['DELETE'])
@jwt_required()
def delete_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"}), 200
    else:
        return jsonify({"message": "Book not found"}), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
