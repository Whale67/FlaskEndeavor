from flask import Flask, render_template, redirect, request, url_for, flash
import os
from os import environ
from send_email import send_email
from flask_wtf import FlaskForm
from wtforms import TextField, validators, HiddenField
from wtforms import TextAreaField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

class ContactForm(FlaskForm):
   firstName = TextField('First Name', validators=[
   			   Required('Hi! I am Naomi and you are?'),
   			   ])
   lastName = TextField('Last Name', validators=[
   			   Required('You might as well leave your last name while you are here.'),
   			   ])	
   email = TextField('Email Address', validators=[
           Required('Please provide a valid email address'),
           Length(min=6, message=(u'Email address too short')),
           Email(message=(u'Ummm, I don\'t think that is valid.'))])
   subject = TextField('Subject', validators=[
           Required('A email without a subject is like a present without a bow')])
           
   comments = TextAreaField('Message or Comments', validators=[Required('If you don\'t tell me something I can\'t tell you something')])
 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/journal')
def journal():
	return render_template('journal.html')

@app.route('/portfolio.html')
def portfolio():
	return render_template('portfolio.html')		

@app.route('/contact')
def contact():
	form = ContactForm()
	return render_template('contact.html', form = ContactForm())

@app.route('/about')
def about():
	return render_template('about.html')	

@app.route('/privacy')
def privacy():
	return render_template('privacy.html')

@app.route('/formJournal')
def formJournal():
	return render_template('formJournal.html')	

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html'), 500

@app.route('/send_form', methods=['POST'])
def send_form():
	form = ContactForm()
	if form.validate():
		firstName = form.firstName.data
		lastName = form.lastName.data
		email = form.email.data
		subject = form.subject.data
		comments = form.comments.data
		send_email(firstName, lastName, email, subject, comments)
		return render_template('thankyou.html')	
	flash('Something appears to have been filled out incorrectly. Please try again.')	
	return render_template('contact.html', form=form)	
		
			


if __name__== '__main__':
	app.run()	
