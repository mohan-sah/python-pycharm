from flask import Flask, render_template, request, redirect, url_for

#sql imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import sqlite3
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"

#CREATING A DATABASE
class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///my_books_database.db"

#CREATING EXTENSION
db = SQLAlchemy(model_class = Base)
db.init_app(app)

##CREATING A TABLE
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key = True)
    title: Mapped[str] = mapped_column(String(251),unique= True,nullable= False)
    author:Mapped[str] =  mapped_column(String(250),nullable = False)
    rating: Mapped[float]  =mapped_column(Float,nullable = False)

    #this will allow each books to be identify by it's title when printing
    def __repr__(self):
        return f'Book {self.title}'
with app.app_context():
    db.create_all()
# ## CREATING SOME RECORDS
# with app.app_context():
#     # List of Harry Potter books
#     harry_potter_books = [
#         {'id': 1, 'title': 'Harry Potter and the Philosopher\'s Stone', 'author': 'J.K. Rowling', 'rating': 9.3},
#         {'id': 2, 'title': 'Harry Potter and the Chamber of Secrets', 'author': 'J.K. Rowling', 'rating': 9.2},
#         {'id': 3, 'title': 'Harry Potter and the Prisoner of Azkaban', 'author': 'J.K. Rowling', 'rating': 9.4},
#         {'id': 4, 'title': 'Harry Potter and the Goblet of Fire', 'author': 'J.K. Rowling', 'rating': 9.5},
#         {'id': 5, 'title': 'Harry Potter and the Order of the Phoenix', 'author': 'J.K. Rowling', 'rating': 9.1},
#         {'id': 6, 'title': 'Harry Potter and the Half-Blood Prince', 'author': 'J.K. Rowling', 'rating': 9.3},
#         {'id': 7, 'title': 'Harry Potter and the Deathly Hallows', 'author': 'J.K. Rowling', 'rating': 9.0},
#         {'id': 8, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'rating': 9.0},
#         {'id': 9, 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'author': 'J.R.R. Tolkien',
#          'rating': 9.4},
#         {'id': 10, 'title': 'The Lord of the Rings: The Two Towers', 'author': 'J.R.R. Tolkien', 'rating': 9.3},
#         {'id': 11, 'title': 'The Lord of the Rings: The Return of the King', 'author': 'J.R.R. Tolkien', 'rating': 9.5},
#         {'id': 12, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'rating': 9.2},
#         {'id': 13, 'title': '1984', 'author': 'George Orwell', 'rating': 9.1},
#         {'id': 14, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'rating': 9.4},
#         {'id': 15, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'rating': 9.0},
#         {'id': 16, 'title': 'Brave New World', 'author': 'Aldous Huxley', 'rating': 9.3},
#         {'id': 17, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'rating': 9.2},
#         {'id': 18, 'title': 'Moby Dick', 'author': 'Herman Melville', 'rating': 8.9},
#         {'id': 19, 'title': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', 'author': 'C.S. Lewis',
#          'rating': 9.1},
#         {'id': 20, 'title': 'The Alchemist', 'author': 'Paulo Coelho', 'rating': 9.2},
#         {'id': 21, 'title': 'The Kite Runner', 'author': 'Khaled Hosseini', 'rating': 9.3},
#         {'id': 22, 'title': 'The Book Thief', 'author': 'Markus Zusak', 'rating': 9.4},
#         {'id': 23, 'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'rating': 9.0},
#         {'id': 24, 'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'rating': 9.1},
#         {'id': 25, 'title': 'The Secret Garden', 'author': 'Frances Hodgson Burnett', 'rating': 8.8},
#         {'id': 26, 'title': 'Little Women', 'author': 'Louisa May Alcott', 'rating': 9.0},
#         {'id': 27, 'title': 'The Bell Jar', 'author': 'Sylvia Plath', 'rating': 9.2},
#         {'id': 28, 'title': 'The Fault in Our Stars', 'author': 'John Green', 'rating': 9.1}
#
#     ]
#
#     # Add each book to the session and commit
#     for book in harry_potter_books:
#         new_book = Books(id=book['id'], title=book['title'], author=book['author'], rating=book['rating'])
#         db.session.add(new_book)
#         db.session.commit()
all_books = []
# READ ALL RECORDS
def see_books():
    global all_books
    with app.app_context():
        books_table = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
        all_books = [{'id': book.id,
                      'title': book.title,
                      'author': book.author,
                      'rating': book.rating, }
                     for book in books_table]


@app.route('/')
def home():
    see_books()
    return render_template('index.html', books = all_books)


@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Books(title = request.form['name'] ,
                             author= request.form['author'],
                             rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        see_books()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<int:book_id>",methods = ["GET","POST"])
def edit_rating(book_id):
    with app.app_context():
        book = db.session.execute(db.select(Books).filter_by(id=book_id)).scalar_one_or_none()
        if book:
            if request.method == 'POST':
                new_rating = request.form.get('rating')
                book.rating = new_rating
                db.session.commit()
                return redirect(url_for('home'))
            else:
                print("error1: form not sent")
                return render_template('edit_rating.html', book=book)
        else:
            print('book not found')
            return redirect(url_for('home'))


@app.route('/<int:book_id>',methods = ["GET","POST"])
def delete_book(book_id):
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

