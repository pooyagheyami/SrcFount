#In the name of GOD
#! use/bin/env python

from flask import Flask, render_template, request, redirect , url_for , json
from flask import send_from_directory
import os

# from flask_mail import Mail, Message
from jinja2 import TemplateNotFound
from wxsq import wxsqins
import gene

import csv
import smtplib
from email.message import EmailMessage

# configure app
app = Flask(__name__)


app.config.from_object(__name__)


@app.route("/")
@app.route("/index.html")
def index():
    title='SrcFount'
    try:
        return render_template("index.html", mytitle=title)
    except TemplateNotFound:
        return 'I Do Not Find This page' #abort(404)

@app.route("/terms-conditions.html")
def terms():
    title='SrcFount-terms'
    try:
        return render_template("terms-conditions.html")
    except TemplateNotFound:
        return 'I Do Not Find This Page'

@app.route("/privacy-policy.html")
def privacy():
    title='SrcFount-privacy'
    try:
        return render_template("privacy-policy.html")
    except TemplateNotFound:
        return 'I Do Not Find This Page'


@app.route("/enrol",methods=['POST','GET'])
def enrol():
    name = request.form['name']
    emil = request.form['email']
    phon = request.form['phone']
    slct = request.form['select']
    term = request.form['terms']
    #print(name,emil,phon,slct,term)
    if term == "Agreed-to-Terms":
        mygn = gene.Gnrat_name(name,phon)
        if mygn == '':
            print("id has exist")
        else:
            mydata = [mygn[0] , name , emil , phon , slct , mygn[1] ]
            wxsqins("SF.db","member"," memid , name , email , phone , slect , dirct ",mydata)

    return render_template('/enrol/member.html')

@app.route('/enrol/member.html?<name>')
def member(name):

    return render_template('/enrol/member.html', name=name)


@app.route('/Memform.html', methods=['POST', 'GET'])
def Memform():
    print('YOU are HERE')
    if request.method == 'POST':

        return redirect(url_for('member', name = request.form['name']))
    else:
        print('Not post')
    return render_template('/Memform.html')




if __name__ == '__main__':
    app.run()