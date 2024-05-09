import sqlite3
from models import User, BlogPost, Comment, Achievement, Service

conn = sqlite3.connect('personal_website.db')
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

    # Check if the email already exists
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Error: Email address already exists. Please choose a different email.")
        return

    # Create a new user object
    new_user = User(username, email, password)
    new_user.save()
    print("User registered successfully!")

# function to login user
def login_user():
    print("User Login")
    username_email = input("Enter username or email: ")
    password = input("Enter password: ")

    # Connect to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Check if the provided username or email exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username_email, username_email))
    user = cursor.fetchone()

    if user:
        # Verifying the password
        if user[3] == password:
            print("Login successful!")
        else:
            print("Invalid password. Please try again.")
    else:
        print("User not found. Please register if you don't have an account.")

    


##calling the functions
register_user()
login_user()

# Close the connection
conn.close()