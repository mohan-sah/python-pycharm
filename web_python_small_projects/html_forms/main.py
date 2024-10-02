from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login",methods= ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username,password = request.form['username'], request.form['password']
        return f"<h1>{username},{password}/n💪💪🏻🧍🏋️ | all working fine</h1>"
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)