from flask import Flask,render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,title varchar(250) NOT NULL UNIQUE,  author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO books VALUES(1,'Harry Potter','J.K.Rowling','9.3')")
# # db.commit()

app =  Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"

# CREATING DATABASE
class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///new-books-collection.db"

#CREATING EXTENSION
db = SQLAlchemy(model_class = Base)
db.init_app(app)

##CREATING TABLE
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key = True)
    title: Mapped[str] = mapped_column(String(250),unique = True,nullable=False)
    author: Mapped[str] = mapped_column(String(250),nullable = False)
    rating: Mapped[float] = mapped_column(Float, nullable = False)# Mappped[Optional[int]] = null, if removed =  not null

    # this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'Book {self.title}'

# # create  table schema in the database. Requires application context.
# with app.app_context():
#     db.create_all()
#
# # CREATE RECORD
# with app.app_context():
#     new_book = Books(id=1, title = 'Harry Potter', author = 'J.K.Rowling',rating = 9.3  ) #id can be auto-generated
#     db.session.add(new_book)
#     db.session.commit()


# READ ALL RECORDS
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

# #READ A PARTICULAR RECORD BY QUERY
# with app.app_context():
#     book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
#
# #UPDATE A PARTICULAR RECORD BY QUERY
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")
#                                     ).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# #UPDATE A RECORD BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Books,book_id)
#     book_to_update.title = "Harry Potter and the Philosopher\'s Stone"
#     db.session.commit()

# DELETE A PARTICULAR RECORD BY PRIMATY KEY
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book,book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

# @app.route("/users")
# def user_list():
#     users = db.session.execute(db.select(User).order_by(User.username)).scalars()
#     return  render_template("user/list.html", users = users)
#
# @app.route("/users/create",methods = ["GET","POST"])
# def user_create():
#     if request.method == "POST":
#         user = User(
#             username = request.form["username"],
#             email = request.form["email"],
#
#         )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for("user_detail",id = user.id))
#     return render_template("user/create.html")
#
# @app.route("/user/<int:id>")
# def user_detail(id):
#     user=db.get_or_404(User,id)
#     return render_template("user/detail.html",user= user)


# @app.route("/user/<int:id>/delete",methods=["GET","POST"])
# def user_delete(id):
#     user = db.get_or_404(User, id)
#     if request.method == "POST":
#         db.session.delete(user)
#         db.session.commit()
#         return redirect(url_for("user_list"))
#     return render_template("user/delete.html",user= user)
