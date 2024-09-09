from flask import Flask

app = Flask(__name__)

print(__name__)


# def html_decorater(function):
#     def wrapper(*args,**kwargs):
#         if function.__name__ == "make_emphasis":
#             return  '<em> {text} </em>'
#     return wrapper
#

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper
def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper
def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper
# make_emphasis
# make_bold
# make_underlined

@app.route('/')
def hello():
    return "<h1 style = 'text-align : center'>Hello, World!</h1>"

@app.route('/bye')
@make_emphasis
@make_bold
@make_underline
def bye():
    return "yooo bye!"

##Different routes using the app.route decorator
@app.route('/bye/bye')
def still_here():
    return "broo, you still here?"

#in this way i can probabaly create many pages for that user or group
#creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet_user(name, number):
    return (f"Hello, {name+'12'}."
            "\nHow can i help you with?"
            f"\nYou have ${number} for credit power left")

if __name__ == '__main__':
    app.run(debug=True)