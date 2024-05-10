#my classes will be User, Blogpost, Comment, portfolio, service
# user is for anyone that interacts with my website
#blogpost is for my publications - poetry and other writeups: title, content, creation date and categories
# #comments by users
# Portfolio.
# Service are the services I offer. title and description.
import sqlite3
from datetime import datetime

#create/connect to my database
conn = sqlite3.connect('personal_website.db')
#create a cursor
cursor = conn.cursor()

#Create Tables - users, blog posts and comment
#user table with id, username, email and password
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE NOT NULL,
                   email TEXT UNIQUE NOT NULL,
                   password TEXT NOT NULL
                )
                ''')
#my blog post table with id, title, content, created_at, user_id
cursor.execute('''
               CREATE TABLE IF NOT EXISTS blog_posts (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   content TEXT NOT NULL,
                   created_at TIMESTAMP NOT NULL,
                   user_id INTEGER NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
                   )
                ''')
#comments table with id, content, created_at, user_id
cursor.execute('''
               CREATE TABLE IF NOT EXISTS comments (
                   id INTEGER PRIMARY KEY,
                   content TEXT NOT NULL,
                   created_at TIMESTAMP NOT NULL,
                   user_id INTEGER NOT NULL,
                   post_id INTEGER NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id),
                   FOREIGN KEY (post_id) REFERENCES blog_posts (id)
                   )
                ''')
#portfolio table with id, title, description, user_id
cursor.execute('''
               CREATE TABLE IF NOT EXISTS skills (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   skill_name TEXT NOT NULL,
                   expertise_level TEXT NOT NULL
                   )
                ''')
#services table with id, title, description, user_id
cursor.execute('''
               CREATE TABLE IF NOT EXISTS services (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   description TEXT NOT NULL,
                   user_id INTEGER NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
                   )
               ''')

# model classes
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                       (self.username, self.email, self.password))
        conn.commit()

class BlogPost:
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.user_id = user_id

    def save(self):
        cursor.execute('INSERT INTO blog_posts (title, content, created_at, user_id) VALUES (?, ?, ?, ?)',
                       (self.title, self.content, self.created_at, self.user_id))
        conn.commit()

class Comment:
    def __init__(self, content, user_id, post_id):
        self.content = content
        self.created_at = datetime.now()
        self.user_id = user_id
        self.post_id = post_id

    def save(self):
        cursor.execute('INSERT INTO comments (content, created_at, user_id, post_id) VALUES (?, ?, ?, ?)',
                       (self.content, self.created_at, self.user_id, self.post_id))
        conn.commit()
        
class Skill:
    def __init__(self, skill_name, expertise_level):
        self.skill_name = skill_name
        self.expertise_level = expertise_level
    
    def save(self):
        cursor.execute('''
            INSERT INTO skills (skill_name, expertise_level) VALUES (?, ?)
        ''', (self.skill_name, self.expertise_level))

        conn.commit()
        conn.close()
        
    
