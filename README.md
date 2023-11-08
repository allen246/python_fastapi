# python_fastapi
User Accoun# FastAPI User Registration and Profile Retrieval

This project demonstrates how to create a user registration API using FastAPI and PostgreSQL. Users' information is stored in two tables: `Users` for personal details (Full Name, Email, Password, Phone) and `Profile` for profile pictures. 
This README provides instructions on setting up and running the application.

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Git
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Docker

## Setup

Clone the repository:
   git clone https://github.com/allen246/python_fastapi.git
   cd python_fastapi
   docker-compose up

## To get started

Open your browser

   Open http://0.0.0.0:8000/docs
   Register a new user
   Login in with that credentials and it will create a JWT token which will be saved on your cookies
   
