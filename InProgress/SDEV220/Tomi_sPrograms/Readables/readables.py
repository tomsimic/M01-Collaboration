"""
Program: application.py
Author: Tomi Simic
Last date modified: 2024-04-12
This program is to be used for M04 Lab - Case Study: Python APIs
"""
# pseudo code:
# import needed modules:
# create constants
# configure connection to database
# create books class
# create functions:
#   get_books
#   get_book
#   add_book
#   delete_book


# Importing needed modules:
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy as sa

# Generating constants
APP = Flask(__name__)

# Configure connection to the database:
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = sa(APP)
APP.app_context().push()

# Creating Books class:


class Book(db.Model):
    """Creates the table columns for the library"""
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(30))

    def __repr__(self):
        return f"{self.book_name} by {self.author} published by {self.publisher}"

# Setting default page retrival:


@APP.route('/')
def index():
    """Pulls index.html"""
    return 'Hello! Welcome to Readables: The Webliary'

# Creating function for default data to be submitted to libarary


@APP.route('/books')
def get_books():
    """The virtual library shelfs"""
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'Book title': book.book_name,
                     'Author': book.author, 'Publisher': book.publisher}
        output.append(book_data)
    return {'Books on hand': output}

# Creating function for book retrival


@APP.route('/books/<id>')
def get_book(id):
    """Replies to book reqests"""
    book = Book.query.get_or_404(id)
    return {"Book title": book.book_name, "Author": book.author, "Published by:": book.publisher}

# Creating function to add books through web interface:


@APP.route('/books', methods=['POST'])
def add_book():
    """Adding books to Webliary through web interface"""
    book = Book(book_name=request.json['book_name'],
                author=request.json['author'],
                publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Creating function to remove books:


@APP.route('/books/<id>', methods=['DELETE'])
def remove_book(id):
    """This shouldn't really exist since book burning is immoral"""
    book = Book.query.get(id)
    if book is None:
        return {"error": "That book is not found in this Webliary"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "The book has been burned, blasphemer"}
