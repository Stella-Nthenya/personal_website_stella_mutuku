# Personal Website CLI with ORM

This is a command-line interface (CLI) application for managing a personal website. It provides functionalities for user registration, login, blog post management, comment management, portfolio management, and service management. Additionally, it utilizes an Object-Relational Mapping (ORM) approach for interacting with the SQLite database.

## Setup

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Run the `cli.py` file to start the application.

## Usage

### User Management

- **Register a New User**: Allows users to create a new account by providing a username, email, and password.
- **Login User**: Enables existing users to log in using their username/email and password.

### Blog Post Management

- **Add a Blog Post**: Lets users add a new blog post by providing a title, content, and user ID.
- **View Blog Posts**: Displays all existing blog posts.
- **Delete Blog Post**: Allows users to delete a specific blog post by its title.

### Skills Management
- **Add Skill**: Users can add new skills to their portfolio.
- **List Skills**: Displays all skills in the user's portfolio.
- **Delete Skill**: Allows users to remove skills from their portfolio.

## Database

This application uses SQLite as its database. It contains tables for users, blog posts and skills

## Model Classes

- **User**: Represents a user of the application. It includes properties for username, email, and password.
- **BlogPost**: Represents a blog post with properties such as title, content, creation date, and user ID.
- **Comment**: Represents a comment on a blog post. It includes properties for content, creation date, user ID, and post ID.
- **Skill**: Represents a skill in the user's portfolio, with properties for skill name and expertise level.
