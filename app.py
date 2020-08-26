#In the name of GOD
#! use/bin/env python

from flask import Flask, render_template, request, redirect , url_for , json
import os
from time import sleep
from werkzeug.utils import secure_filename
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
app.config['UPLOAD_FOLDER'] = os.getcwd()+'\\'+'members\\'

mmdata = []
mmid = ''
mmdr = ''

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
    #title='SrcFount-terms'
    try:
        return render_template("terms-conditions.html")
    except TemplateNotFound:
        return 'I Do Not Find This Page'

@app.route("/privacy-policy.html")
def privacy():
    #title='SrcFount-privacy'
    try:
        return render_template("privacy-policy.html")
    except TemplateNotFound:
        return 'I Do Not Find This Page'

@app.route("/Memform.html",methods=['POST','GET'])
def memform():
    sleep(3)
    #print(mmdata)
    if request.method == 'POST' :
        #print(request.files)
        insert(request.form,mmid)
        insinfo(request.form,mmid)
        if 'file1' in request.files:
            file = request.files['file1']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], mmdr+'\\'+filename))
            #print("saved file successfully")
        if 'file2' in request.files:
            file = request.files['file2']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], mmdr + '\\' + filename))
            #print("saved file successfully")

        return "success send form"

    else:
        try:
            return render_template("Memform.html",mydata=mmdata)
        except TemplateNotFound:
            return 'I Do Not Find This Page'



def insert(data,mid):
    D0 = mid
    D1 = data['srefr']
    D2 = data['nrefr']
    D3 = data['sdata']
    D4 = data['ndata']
    D5 = data['sftur']
    D6 = data['nftur']
    recrd = [D0,D1,D2,D3,D4,D5,D6]
    wxsqins("SF.db","request","memid, refr_serv, refr_need, data_serv, data_need, ftur_serv, ftur_need ", recrd)


def insinfo(data,mid):
    D0 = mid
    D1 = data['mweb']
    if 'http' in D1:
        tid = '001'
    else:
        tid = '002'
    rcord = [D0,D1,tid]
    wxsqins("SF.db","meminfo","memid , info , titid ", rcord)

@app.route("/enrol",methods=['POST','GET'])
def enrol():
    name = request.form['name']
    emil = request.form['email']
    phon = request.form['phone']
    slct = request.form['select']
    term = request.form['terms']
    global mmdata,mmid,mmdr
    mmdata = request.form
    #print(name,emil,phon,slct,term)
    if term == "Agreed-to-Terms":
        mygn = gene.Gnrat_name(name,phon)
        mmid = mygn[0]
        mmdr = mygn[1]

        if mygn == '':
            return "id has exist"
        else:
            mydata = [mygn[0] , name , emil , phon , slct , mygn[1] ]
            wxsqins("SF.db","member"," memid , name , email , phone , slect , dirct ",mydata)
            return 'success'




if __name__ == '__main__':
    app.run(debug=True,port=5000)