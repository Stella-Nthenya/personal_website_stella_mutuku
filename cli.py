import sqlite3
from models import User, BlogPost, Comment, Achievement, Service

# functions I need
# User - Register, login, view profile, delete account
# The Blog - add, View, Delete and search posts and list posts by category
# Comment -  add, view, edit and delete comment
# Achievement - add, view, edit and delete achievement
# Service - add, view, edit and delete achievement


# Function to connect to the database
def connect_to_db():
    return sqlite3.connect('personal_website.db')

#Register a new user
def register_user():
    print("Register")
    username = input("Enter username: ")
    email = input ("Enter your email: ")
    password = input("Input password: ")
    # Create a new user object
    new_user = User(username, email, password)
    new_user.save()
    print("User registered successfully!")