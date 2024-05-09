import sqlite3
from models import User, BlogPost, Comment, Achievement, Service

conn = sqlite3.connect('personal_website.db')
cursor = conn.cursor()
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
        print("Error: Email address already exists. Login instead!")
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

#add post function   
def add_post():
    print("Add a New Blog Post")
    title = input("Enter the title of the post: ")
    user_id = input("Enter your user ID: ")

    print("Enter post content (press Enter twice to finish):")
    content_lines = []
    while True:
        line = input()
        if line:
            content_lines.append(line)
        else:
            break
    content = '\n'.join(content_lines)

    post = BlogPost(title, content, user_id)
    post.save()
    print("Post added successfully!")

def view_posts():
    cursor.execute("SELECT * FROM blog_posts")
    posts = cursor.fetchall()
    if posts:
        for post in posts:
            print(f"Title: {post[1]}\nContent: {post[2]}\nCreated At: {post[3]}")
            print("-------------------------------")
    else:
        print("No posts found.")

def delete_post():
    title = input("Enter the title of the post to delete: ")
    cursor.execute("SELECT id FROM blog_posts WHERE title=?", (title,))
    post = cursor.fetchone()
    if post:
        post_id = post[0]
        cursor.execute("DELETE FROM blog_posts WHERE id=?", (post_id,))
        conn.commit()
        print("Post deleted successfully!")
    else:
        print("Post not found with the given title.")



##calling the functions
# register_user()
# login_user()
# add_post()
# view_posts()
# delete_post()

# Close the connection
conn.close()
