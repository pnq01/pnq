# 📝 FastAPI JournalBlog

A lightweight blog system built with FastAPI, supporting user registration, login, and full CRUD operations for articles. Ideal for learning FastAPI, JWT authentication, and SQLAlchemy ORM in a real-world scenario.

---

## 🚀 Features

- ⚡ High-performance asynchronous RESTful API with FastAPI
- 🧱 SQLAlchemy for database ORM
- 🔐 JWT-based authentication system
- 🧩 Modular project structure for scalability
- 📄 Interactive API documentation (Swagger UI & Redoc)

---

## 🧰 Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- JWT

---

## 📁 Project Structure

```text
fastapi_journalblog/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point with FastAPI app
│   ├── models/              # SQLAlchemy models
│   ├── routers/             # API route modules (user, blog, etc.)
│   ├── schemas/             # Pydantic data models
│   └── services/            # Business logic and utilities
├── tests/                   # Unit tests
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
