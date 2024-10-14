from flask import Flask, render_template,redirect

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired,Length,Email
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class MyForm(FlaskForm):
    name = StringField("name",[DataRequired(message="yooo! i feel lonely"),Length(min=2, max=30,message="come on! that possibly can't be your name.")])
    email = EmailField("E-mail", validators=[DataRequired(message="bhai, mail kaise bhul gaya?"), Email()] )
    password = PasswordField("password", validators=[DataRequired(message="yooo! password missing hai"), Length(min=8, max=40)])
    login =  SubmitField(label = "login",render_kw={"class": "btn btn-primary btn-lg"})

app = Flask(__name__)
app.secret_key = "some secret string"



@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods = ["GET","POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    print(form.email.data)
    if form.validate_on_submit():
        if (form.email.data == "admin@email.com")& (form.password.data == "12345678"):
            print("yes")
            return render_template("success.html")
        else :
            return render_template("denied.html")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
