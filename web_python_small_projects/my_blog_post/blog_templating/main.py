from flask import Flask, render_template
import requests


app = Flask(__name__)
all_post_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
@app.route('/')
def home():
    # all_post_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", all_post =all_post_response)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    clicked_post = all_post_response[post_id-1]
    return render_template("post.html", post =clicked_post)

if __name__ == "__main__":
    app.run(debug=True)
