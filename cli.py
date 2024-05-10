import sqlite3
from models import User, BlogPost, Skill

conn = sqlite3.connect('personal_website.db')
cursor = conn.cursor()
# functions I need
# User - Register, login, view profile, delete account
# The Blog - add, View, Delete and search posts and list posts by category
# Comment -  add, view, edit and delete comment
# portfolio - add, view, edit and delete portfolio
# Service - add, view, edit and delete portfolio


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

#add a blogpost function   
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
#view blog posts function 
def view_posts():
    cursor.execute("SELECT * FROM blog_posts")
    posts = cursor.fetchall()
    if posts:
        for post in posts:
            print(f"Title: {post[1]}\nContent: {post[2]}\nCreated At: {post[3]}")
            print("-------------------------------")
    else:
        print("No posts found.")
#delete a blog post function 
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

#skills and expertise
def add_skill():
    skill_name = input("Enter the skill name: ")
    expertise_level = input("Enter the expertise level: ")
    
    skill = Skill(skill_name, expertise_level)
    skill.save()
    print(f"Skill '{skill_name}' added successfully.")

def list_skills():
    cursor.execute("SELECT * FROM skills")
    skills = cursor.fetchall()

    if skills:
        print("Skills:")
        for skill in skills:
            print(f"Skill Name: {skill[1]}, Expertise Level: {skill[2]}")
    else:
        print("No skills found.")

def delete_skill():
    # Prompt the user for the skill name to delete
    skill_name = input("Enter the skill name to delete: ")

    cursor.execute("SELECT id FROM skills WHERE skill_name=?", (skill_name,))
    skill = cursor.fetchone()

    if skill:
        skill_id = skill[0]
        cursor.execute("DELETE FROM skills WHERE id=?", (skill_id,))
        conn.commit()
        print(f"Skill '{skill_name}' deleted successfully!")
    else:
        print(f"Skill '{skill_name}' not found.")



#calling the functions
# register_user()
# login_user()
# add_post()
# view_posts()
# delete_post()
# add_skill()
# list_skills()
# delete_skill()
# list_skills()

# Close the connection
conn.close()
