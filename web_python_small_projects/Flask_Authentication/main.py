import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB  with the UserMixin
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __repr__(self):
        return '<User %r>' % self.email


with app.app_context():
    db.create_all()


def hashed_and_salted_password(password):
    return generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", 'POST'])
def register():
    if request.method == 'POST':
        already_user = User.query.filter_by(email=request.form['email']).first()
        print(already_user)
        if already_user:
            print('already user')
            flash('You already signed up with that email, log in instead', 'danger')
            return redirect(url_for('login'))
        new_user = User(
            email=request.form['email'],
            name=request.form['name'],
            password=hashed_and_salted_password(request.form['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        # Can redirect() and get name from the current_user
        return redirect(url_for('secrets',logged_in = True))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        email = request.form.get('email')
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password, password):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets',logged_in = True))
    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name,logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download',methods = ['POST'])
@login_required
def download():
    return send_from_directory('static/files', "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
