from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['CKEDITOR_CONFIG'] = {'versionCheck': False}
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class NewPostForm(FlaskForm):
    blog_title = StringField("Blog Title", [DataRequired(message="empty!"),
                                            Length(min=0, max=400, message="that title is something??")])
    subtitle = StringField("Subtitle", [DataRequired(message="empty!"),
                                        Length(min=0, max=400, message="that some subtitle you got there !")])
    your_name = StringField("Your Name",
                            [DataRequired(message="empty!"), Length(min=0, max=50, message="oh that the name??")])
    blog_img_url = StringField("Blog Img URL", [DataRequired(message="empty!"), URL()])
    blog_content = CKEditorField('Blog Content')
    submit_post = SubmitField(label="SUBMIT POST", render_kw={"class": "btn btn-primary btn-lg"})


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    posts = []
    with app.app_context():
        posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars().all()
    return render_template("index.html", all_posts=posts)


#  Add a route so that can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# add_new_post() to create a new blog post

@app.route('/new-post', methods=["GET", 'POST'])
def add_new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        with app.app_context():
            new_post = BlogPost(
                title=form.blog_title.data,
                subtitle=form.subtitle.data,
                date=datetime.now().strftime("%B %d,%Y"),
                body=form.blog_content.data,
                author=form.your_name.data,
                img_url=form.blog_img_url.data,
            )
            db.session.add(new_post)
            db.session.commit()
            new_post_id = new_post.id

            return redirect(url_for("show_post", post_id=new_post_id))
    return render_template("make-post.html", form=form, should_new_post=True)


# edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    with app.app_context():
        post = db.get_or_404(BlogPost, post_id)
        form = NewPostForm(blog_title=post.title,
                           subtitle=post.subtitle,
                           blog_content=post.body,
                           your_name=post.author,
                           blog_img_url=post.img_url, )
        if form.validate_on_submit():
            db.session.query(BlogPost).filter(BlogPost.id == post.id).update({
                "title": form.blog_title.data,
                "subtitle": form.subtitle.data,
                "body": form.blog_content.data,
                "author": form.your_name.data,
                "img_url": form.blog_img_url.data
            })
            db.session.commit()
            return redirect(url_for('show_post', post_id=post.id))
    return render_template('make-post.html', form=form)


# delete_post() to remove a blog post from the database
@app.route('/delete-post/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
