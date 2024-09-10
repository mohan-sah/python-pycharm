from flask import Flask
from random import randint
from links import links

app = Flask(__name__)
print(__name__)

GENERATED_NUMBER = randint(0,9)

def add_css(function):
    def wrapper(*args,**kwargs):
        print("Decorator - Arguments received:", args, kwargs)  # Debug statement
        high_low_statement = function(*args, **kwargs)
        print(high_low_statement)
        answer_number = kwargs.get("answer_number")
        if answer_number < GENERATED_NUMBER:
            return (f"<center><h1 style = 'color:purple'>{high_low_statement}</h1>"
                    f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width = 250 height = 250>{links}</center>" )
        elif answer_number > GENERATED_NUMBER:
            return (f"<center><h1 style = 'color:red'>{high_low_statement}</h1>"
                    f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width = 250 height = 250 >{links}</center>")
        elif answer_number == GENERATED_NUMBER:
            return (f"<div style='text-align: center;'>"
                    f"<h1 style = 'color:green'>{high_low_statement}</h1>"
                    f"<div><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width = 250 height = 250 ></div><br>"
                    f"<div><a href='/' style = 'font-size: 24px;color: #ffffff;background-color: #007bff;padding: 10px 20px;border-radius: 5px;transition: background-color 0.3s, color 0.3s;margin: 20px;outline: none;curson:pointer'>Home</a></div>"
                    f"</div>")
    return wrapper
@app.route("/")
def title():
    global GENERATED_NUMBER
    GENERATED_NUMBER = randint(0,9)
    return ("<center><h1>Guess a number between 0 and 9</h1>"
            f"<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>{links}</center>")


@app.route("/<int:answer_number>")
@add_css
def higher_lower(answer_number):
    print("Route function - Argument received:", answer_number)  # Debug statement

    if answer_number< GENERATED_NUMBER:
        return "too low"
    elif answer_number> GENERATED_NUMBER:
        return "too high"
    else:
        return "you got it right"

if __name__ == "__main__":
    app.run(debug=True)