# install virtual environment
# pip install Flask-mail
#pip install flask
from flask import Flask, render_template
from flask_mail import Mail, Message

app= Flask(__name__)

mail = Mail(app)

#configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Email.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route("/") 
def index(): 
   msg = Message( 
                'Hello', 
                sender ='johnirungumathenge@gmail.com', 
                recipients = ['email1.com','email2@gmail.com'] 
               ) 
   msg.body = 'Hello Flask message sent from Flask-Mail \n welcome to the world of programming'
   mail.send(msg) 
   return 'Sent Mail'

if __name__ == '__main__':
    app.run(debug=True)
