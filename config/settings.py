import os

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@db:5432/todo_db"
)
