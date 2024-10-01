#note: use https://www.npoint.io/docs to create free APIs

from flask import Flask,render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    random_number = randint(0,9)
    CURRENT_YEAR = datetime.now().year
    YOUR_NAME = "Mohan Sah"

    return render_template("index.html",num = random_number, YYYY =CURRENT_YEAR, YOUR_NAME = YOUR_NAME)
@app.route("/guess/<YOUR_NAME>")
def guess_with_name(YOUR_NAME):
    AGE = requests.get(f"https://api.agify.io?name={YOUR_NAME}").json()["age"]
    GENDER = requests.get(f"https://api.genderize.io?name={YOUR_NAME}").json()["gender"]
    YOUR_NAME =YOUR_NAME.title()
    return render_template("guess.html", age = AGE, gender = GENDER , name =YOUR_NAME)

@app.route('/blog/<int:num>')
def get_blog(num):
    all_blog_post = requests.get(f"https://api.npoint.io/c790b4d5cab58020d391").json()
    num = str(num)
    return render_template("blog.html", all_blog_post = all_blog_post, passed_num = num )

if __name__ == "__main__":
    app.run(debug=True)