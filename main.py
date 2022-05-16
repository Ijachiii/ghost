from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

email_address = "jasonfeddd@gmail.com"
password = "Donietello"


class MessageForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")


def send_email(email, message):
    email_message = f"Subject:New Message\n\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email_address, password)
        connection.sendmail(email_address, "davidaudu1010@gmail.com", email_message)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["email"], data["message"])
        return render_template("contact.html")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
