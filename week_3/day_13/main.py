from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError

import datetime

DATABASE_URL = "postgresql+psycopg2://postgres:Kiran246@localhost:5432/advance_db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Define Models (User / Tasks)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    posts = relationship('Post', back_populates='user', cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

Base.metadata.create_all(engine)

#Utility Functions
def get_user_by_email(email):
    try:
        return session.query(User).filter_by(email=email).first()
    except Exception as e:
        print(f"Error querying user: {e}")
        return None

def confirm_action(prompt:str) -> bool:
    response = input(f"{prompt} (yes/no): ").strip().lower()
    return response == 'yes'

#CRUD
def add_user():
    name,email,age = input("Enter user name: "), input("Enter the email: "), int(input("Enter user age: "))
    if get_user_by_email(email):
        print(f'User already exists: {email}')
        return

    try:
        session.add(User(user_name=name, email=email, age=age))
        session.commit()
        print(f'User: {name} added')
    except IntegrityError:
        session.rollback()
        print(f"ERROR")

def add_post():
    email = input("Enter the email of user to add tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f'No user found with that email')
        return

    title, content = input("Enter title: "), input("Enter content: ")
    session.add(Post(title=title, content=content, user_id=user.id))
    session.commit()
    print(f'Added to the database: {title}:{content}')

def query_user():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.user_name}, Age: {user.age}, Email: {user.email}")

def query_posts():
    email = input("Enter the email id of the post: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return
    for post in user.posts:
        print(f"Post ID: {post.user_id}, Title: {post.title}, Content: {post.content}")

def update_user():
    email = input("Enter the email id of the user: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return

    user.user_name = input("Enter the name (leave blank to remain as it is): ") or user.user_name
    user.email = input("Enter the email (leave blank to remain as it is): ") or user.email
    age = input("Enter the age (leave blank to remain as it is): ") or user.age
    if(age != ''):
        user.age = int(age)
    session.commit()
    print("User has been updated!")

def delete_user():
    email = input("Enter the email id of the user to delete: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return

    if confirm_action(f"Confirm yes or no to delete: {user.user_name}?"):
        session.delete(user)
        session.commit()
        print("User has been deleted")

def delete_post():
    email = input("Enter the email of the post: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return

    if not user.posts:
        print("No posts found for this user")
        return

    for post in user.posts:
        print(f"POST ID: {post.post_id}, Title: {post.title}")

    pid_input = input("Enter the post id to delete the post: ").strip()
    if not pid_input.isdigit():
        print("Invalid post id")
        return

    pid = int(pid_input)
    post = next((p for p in user.posts if p.post_id == pid), None)
    if not post:
        print("No post found with that id")
        return

    if confirm_action(f"Confirm yes or no to delete post: {post.post_id}?"):
        session.delete(post)
        session.commit()
        print("Post has been deleted")
    else:
        print("Post deletion cancelled")


def main():
    while True:
        print("1.add_user\n2.add_post\n3.query user\n4.query post")
        print("5.update user\n6.delete user\n7.delete post\n8.Exit")
        choice = int(input("Select your process:"))

        match choice:
            case 1:
                add_user()
            case 2:
                add_post()
            case 3:
                query_user()
            case 4:
                query_posts()
            case 5:
                update_user()
            case 6:
                delete_user()
            case 7:
                delete_post()
            case 8:
                break
            case _:
                print("wrong option")
                break

main()