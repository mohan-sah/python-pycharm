from flask import Flask,render_template
import requests
 

# take data from here "https://api.npoint.io/7495458f5307404ee89f"
response = requests.get("https://api.npoint.io/7495458f5307404ee89f").json()

app = Flask(__name__)
print(__name__.split)


@app.route('/')
def home():
    
    return render_template('index.html', all_blog_post = response)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',post_id=id, all_blog_post = response)


if __name__ == '__main__':
    app.run(debug=True)

