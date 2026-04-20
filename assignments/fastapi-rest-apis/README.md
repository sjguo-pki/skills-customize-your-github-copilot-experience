# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build and test a simple REST API using FastAPI to practice routing, request/response handling, and basic data validation.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Create a FastAPI app with endpoints to manage a small in-memory collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by ID.
- Return a `404` error response when a requested book is not found.


### 🛠️ Add Create and Update Operations

#### Description
Extend the API so users can add new books and update existing ones with validated request data.

#### Requirements
Completed program should:

- Define a Pydantic model for book input data.
- Implement `POST /books` to add a new book and return the created record.
- Implement `PUT /books/{book_id}` to update title and author fields.
- Validate required fields and keep IDs unique.
- Example request body:
  ```json
  {
    "title": "Clean Code",
    "author": "Robert C. Martin"
  }
  ```
