import ast

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from Movie_search import MovieSearch

from wtforms import Form, StringField,SubmitField, IntegerField,FloatField,URLField,validators


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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
movie = MovieSearch()

# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#initialize-the-extension
# INITIALIZE THE EXTENSION
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_database.db"
db.init_app(app)


# CREATE DB
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True,)
    title: Mapped[str] = mapped_column(String(250),unique=True)
    year: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column()


# CREATE TABLE

with app.app_context():
    db.create_all()

all_movies = []

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie", name="form_type")


class MovieEditForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=250)])
    year = IntegerField('Year', [validators.NumberRange(min=1800, max=2050)])
    description = StringField('Description', [validators.Length(max=500)])
    rating = FloatField('Rating', [validators.NumberRange(max=10)])
    ranking = IntegerField('Ranking', )
    review = StringField('Description', [validators.Length(max=500)])
    img_url = URLField ("Image URL", [validators.URL(True)])
    submit = SubmitField('Done')

def fetch_all_movies():
    global all_movies
    with app.app_context():
        movie_table = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
        total_entries = db.session.execute(db.select(db.func.count(Movie.id))).scalar()
        all_movies = [
            {
                "title" : movie.title,
                "year" : movie.year,
                "description" : movie.description,
                "rating" : movie.rating,
                "ranking" : total_entries - index,
                "review" : movie.review,
                "img_url" : movie.img_url,
        }
            for index, movie in enumerate(movie_table)
        ]
        #Rank the Movies By Rating




@app.route("/")
def home():
    fetch_all_movies()
    return render_template("index.html", all_movies = all_movies)

@app.route('/add',methods = ['POST',"GET"])
def add():
    form = FindMovieForm()
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'add_movie':
            with app.app_context():
                new_movie = Movie(
                    title=request.form.get('title'),
                    year=request.form.get('year'),
                    description=request.form.get('description'),
                    rating=request.form.get('rating'),
                    ranking=request.form.get('ranking'),
                    review=request.form.get('review'),
                    img_url=request.form.get('img_url'),
                )
                db.session.add(new_movie)
                db.session.commit()
                fetch_all_movies()
                flash('Movie added successfully!', 'success')
                return redirect(url_for('home'))
        else:

            title = request.form['title']
            print(title)
            flash('Movie title added successfully!', 'success')
            return redirect(url_for('select',title =title))

    return render_template("add.html", form = form)

@app.route('/edit/<edit_title>' , methods = ['POST',"GET"])
def edit(edit_title):
    print('edit_title : ',edit_title)
    edit_form = MovieEditForm()
    movie_to_edit = Movie.query.filter_by(title = edit_title).first_or_404()
    if not movie_to_edit:
        flash('Movie not Found!', "error")
        return redirect(url_for('home'))

    #prepopulating the form
    edit_form = MovieEditForm(obj=movie_to_edit)

    if edit_form.validate_on_submit():
        movie_to_edit.title  = edit_form.title.data
        movie_to_edit.year = edit_form.year.data
        movie_to_edit.description = edit_form.description.data
        movie_to_edit.rating = edit_form.rating.data
        movie_to_edit.ranking = edit_form.ranking.data
        movie_to_edit.review = edit_form.review.data
        movie_to_edit.img_url = edit_form.img_url.data

        db.session.commit()
        flash('Movie updated Successfully!',"success")
        return redirect(url_for('home'))

    return render_template('edit.html', form = edit_form, edit_title = edit_title )

@app.route('/select/<title>',methods = ['POST',"GET"])
def select(title):
    print('enter select', title)
    data = movie.get_movie_by_name(f"{title}")
    if data['total_results']== 0 or data is None:
        return "<h1>No Such Movie Found<h1>"

    return render_template('select.html',data = data)


@app.route("/find")
def find_movie():
    selected_movie = ast.literal_eval(request.args.get('selected_movie'))
    with app.app_context():
        new_movie = Movie(
            title=selected_movie['original_title'],
            year=selected_movie['release_date'].split("-")[0],
            description=selected_movie['overview'],#[:250]
            rating=selected_movie['vote_average'],
            ranking=None,
            review="N/A",
            img_url=f"https://image.tmdb.org/t/p/w500/{selected_movie['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        fetch_all_movies()
        flash('Movie added successfully!', 'success')
        return redirect(url_for('edit',edit_title= selected_movie['original_title'] ))


@app.route('/delete/<delete_title>',methods = ["GET","POST"])
def delete(delete_title):
    with app.app_context():
        movie_to_delete = Movie.query.filter_by(title = delete_title).first_or_404()
        db.session.delete(movie_to_delete)
        db.session.commit()
    flash('Movie deleted Successfully!', "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
