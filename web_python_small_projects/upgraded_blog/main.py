from flask import Flask,render_template,request
import requests
from notification_manager import NotificationManager
 

# take data from here "https://api.npoint.io/7495458f5307404ee89f"
response = requests.get("https://api.npoint.io/7495458f5307404ee89f").json()

app = Flask(__name__)
print(__name__.split)
notify = NotificationManager()

@app.route('/')
def home():
    
    return render_template('index.html', all_blog_post = response)

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',post_id=id, all_blog_post = response)

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)
        name = data['name']
        email =data['email']
        phoneno =data['phoneno']
        message =data['message']
        print(name, email, phoneno, message)
        notify.send_emails(receive_mail="mohansah.100daysofcode@gmail.com", message_body=f"Subject: MY WEBSITE \n\nname = {data['name']}\nemail ={data['email']}\nphoneno ={data['phoneno']}message ={data['message']}")
        return render_template('contact.html',msg_sent = True)
    else: return render_template('contact.html',msg_sent = False)


if __name__ == '__main__':
    app.run(debug=True)

