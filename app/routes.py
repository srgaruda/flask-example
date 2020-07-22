from flask import render_template
from flask import request
from app import app
from app.forms import LoginForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl



@app.route('/contact')
def login():
    form = LoginForm()
    return render_template('contact.html', title='Contact Us', form=form)

@app.route('/thanks', methods=["POST"])
def thanks():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    dob = request.form['dob']
    email = request.form['email']
    phone = request.form['phone']
    send_email(firstname,lastname,dob,email,phone)
    return render_template('thanks.html', title='Thank you')

    

def send_email(firstname,lastname,dob,email,phone):
    contact_text = "Received new contact from "+firstname+" "+lastname+".Who can be contacted on "+phone+" or "+email
    mail_content = contact_text
    sender_address = 'sampletestphytoncode@gmail.com'
    sender_pass = 'random1357'
    receiver_address = 'srgaruda@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'New contact information received.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    context = ssl.create_default_context()
    session.starttls(context=context)
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    