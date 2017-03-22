from flask import Flask, url_for, render_template, redirect, current_app
from email.mime.text import MIMEText
import smtplib
#from flask import current_app as app

def send_email(firstName, lastName, email, subject, comments):
	#from_email="aristotle.gizmo@gmail.com"
	#from_password = "26r-Ncg-s6d-Wat"
	#to_email='codegizmo@protonmail.com' 
	from_email = current_app.config['FROM_EMAIL']
	from_password = current_app.config['FROM_PASSWORD']
	to_email = current_app.config['TO_EMAIL']

	my_subject="codeGizmo Form Data"
	message = "First Name: %s <br> Last Name: %s <br> Email: %s <br> Subject: %s <br> Message: %s" % (firstName, lastName, email, subject, comments)

	msg=MIMEText(message, 'html')
	msg['Subject']=my_subject
	msg['To']=to_email
	msg['From']=from_email

	gmail=smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)
