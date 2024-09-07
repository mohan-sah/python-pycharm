from flask import Flask

app = Flask(__name__)

print(__name__)
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/bye')
def bye():
    return "yooo bye!"
@app.route('/bye/bye')
def still_here():
    return "broo, you still here?"

if __name__ == '__main__':
    app.run()