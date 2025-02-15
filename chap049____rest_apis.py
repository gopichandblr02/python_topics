# """
# Python REST API with Examples
# A REST API (Representational State Transfer Application Programming Interface) allows applications to communicate over HTTP.
# In Python, we can create REST APIs using Flask or FastAPI.
#
# 1. Creating a REST API Using Flask
# Step 1: Install Flask
# """
# pip install flask
#
# # Step 2: Create a Simple Flask API
#
# from flask import Flask, jsonify
# app = Flask(__name__)
# @app.route('/hello', methods=['GET'])
# def hello():
#     return jsonify({"message": "Hello, World!"})
#
# if __name__ == '__main__':
#     app.run(debug=True)
# # Run the API:
# python app.py
#
# # Test it in the browser or Postman:
# http://127.0.0.1:5000/hello
#
# # Output (JSON Response)
# # {
# #     "message": "Hello, World!"
# # }
#
# 2. REST API with CRUD Operations (Flask)
# Let's build a REST API for managing a list of books.
#
# Step 1: Install Flask
# sh
# Copy
# Edit
# pip install flask
# Step 2: Create app.py
# python
# Copy
# Edit
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# # Sample data
# books = [
#     {"id": 1, "title": "1984", "author": "George Orwell"},
#     {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"}
# ]
#
# # GET all books
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)
#
# # GET a book by ID
# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     return jsonify(book) if book else ("Book not found", 404)
#
# # POST (Add a new book)
# @app.route('/books', methods=['POST'])
# def add_book():
#     data = request.get_json()
#     new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
#     books.append(new_book)
#     return jsonify(new_book), 201
#
# # PUT (Update an existing book)
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book:
#         data = request.get_json()
#         book.update(data)
#         return jsonify(book)
#     return ("Book not found", 404)
#
# # DELETE a book
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [b for b in books if b["id"] != book_id]
#     return ("", 204)
#
# if __name__ == '__main__':
#     app.run(debug=True)
# API Endpoints
# Method	Endpoint	Description
# GET	/books	Get all books
# GET	/books/<id>	Get a book by ID
# POST	/books	Add a new book
# PUT	/books/<id>	Update a book
# DELETE	/books/<id>	Delete a book
# Test with cURL
# Get all books
# sh
# Copy
# Edit
# curl http://127.0.0.1:5000/books
# Add a new book
# sh
# Copy
# Edit
# curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "The Hobbit", "author": "J.R.R. Tolkien"}'
# Update a book
# sh
# Copy
# Edit
# curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "Animal Farm"}'
# Delete a book
# sh
# Copy
# Edit
# curl -X DELETE http://127.0.0.1:5000/books/1
# 3. Creating a REST API Using FastAPI
# FastAPI is a modern web framework for building APIs in Python.
#
# Step 1: Install FastAPI and Uvicorn
# sh
# Copy
# Edit
# pip install fastapi uvicorn
# Step 2: Create main.py
# python
# Copy
# Edit
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}
# Run the FastAPI Server
# sh
# Copy
# Edit
# uvicorn main:app --reload
# Test it in the browser:
# cpp
# Copy
# Edit
# http://127.0.0.1:8000
# Interactive API Docs
# FastAPI automatically generates API documentation at:
#
# Swagger UI: http://127.0.0.1:8000/docs
# Redoc: http://127.0.0.1:8000/redoc
# 4. REST API with CRUD (FastAPI)
# python
# Copy
# Edit
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
#
# app = FastAPI()
#
# # Sample data
# books = [
#     {"id": 1, "title": "1984", "author": "George Orwell"},
#     {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"}
# ]
#
# class Book(BaseModel):
#     title: str
#     author: str
#
# # GET all books
# @app.get("/books")
# def get_books():
#     return books
#
# # GET book by ID
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     book = next((b for b in books if b["id"] == book_id), None)
#     if book is None:
#         raise HTTPException(status_code=404, detail="Book not found")
#     return book
#
# # POST (Add a new book)
# @app.post("/books")
# def add_book(book: Book):
#     new_book = {"id": len(books) + 1, "title": book.title, "author": book.author}
#     books.append(new_book)
#     return new_book
#
# # PUT (Update an existing book)
# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: Book):
#     for b in books:
#         if b["id"] == book_id:
#             b["title"] = book.title
#             b["author"] = book.author
#             return b
#     raise HTTPException(status_code=404, detail="Book not found")
#
# # DELETE a book
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     global books
#     books = [b for b in books if b["id"] != book_id]
#     return {"message": "Book deleted"}
# Why Use FastAPI?
# ✅ Faster execution than Flask.
# ✅ Auto-generated API documentation.
# ✅ Asynchronous support (async/await) for high-performance apps.
#
# Which One to Choose?
# Feature	Flask	FastAPI
# Speed	Slower	Faster
# Async Support	Limited	Full async support
# API Documentation	Manual	Automatic Swagger UI
# Performance	Moderate	High
# If you want simplicity, use Flask.
# If you need high performance and async support, use FastAPI.