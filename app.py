

from flask import Flask, render_template, request, redirect
# from flask_mail import Mail, Message
from jinja2 import TemplateNotFound

import csv
import smtplib
from email.message import EmailMessage

# configure app
app = Flask(__name__)

app.config.from_object(__name__)

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return 'I Do Not Find This page' #abort(404)


if __name__ == '__main__':
    app.run()