from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_USERNAME'] = os.getenv('hamoodys2@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('lfkg gipx tzpo rcoy')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hamoodys2@gmail.com'
app.config['MAIL_PASSWORD'] = 'lfkggipxtzporcoy'
app.config['MAIL_DEFAULT_SENDER'] = 'hamoodys3@yahoo.com'

mail = Mail(app)

projects = [
    {"name": "Flask Portfolio", "url": "https://github.com/your-github/flask-portfolio", "description": "A personal portfolio built with Flask."},
    {"name": "Cybersecurity Toolkit", "url": "https://github.com/your-github/cyber-toolkit", "description": "A collection of cybersecurity tools written in Python."},
    {"name": "Network Scanner", "url": "https://github.com/your-github/network-scanner", "description": "A simple network scanner using Python and Scapy."}
]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject=f"New Contact Form Submission from {name}",
                      sender=email,
                      recipients=['hamoodys2@gmail.com'],
                      body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash("Error sending message. Please try again later.", "danger")
            print(e)

    return render_template('contact.html')

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)



