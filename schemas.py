from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField

class RegistrationForm(Form):
    firstname =  StringField('Fistname', [validators.DataRequired()])

    lastname = StringField('Lastname', [validators.DataRequired()])
    
    other_names = StringField('Other Names') 

    email = StringField('Email Address', [validators.DataRequired(),validators.Email(message= "Invalid Email")]) 
    
    phone = StringField("Phone Number",validators = [validators.Length(min=6, max=20)]) 
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
