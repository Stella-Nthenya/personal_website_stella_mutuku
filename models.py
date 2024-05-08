#my classes will be User, Blogpost and Comment


import sqlite3

#create/connect to my database
conn = sqlite3.connect('personal_website.db')
#create a cursor
cursor = conn.cursor()

#Create Tables - users, blog posts and comment

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY
               username TEXT UNIQUE NOT NULL,
               email TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL
               )
               '''
               )

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

# model classes