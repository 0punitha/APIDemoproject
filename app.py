from flask import Flask , render_template, request
from flask_mail import Mail, Message


app = Flask(__name__, template_folder='template')
 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'punithasenthil2019@gmail.com'
app.config['MAIL_PASSWORD'] = 'bczf uszc aeqm ldnd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send_email', methods=["POST"])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=subject, sender=email, recipients=['punithasenthil2019@gmail.com'])
    msg.body = message
    mail.send(msg)
    return 'Email sent successfully'

if __name__=='__main__':
    app.run(debug=True)


