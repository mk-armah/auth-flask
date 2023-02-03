import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask,request,redirect, url_for, requestjsonify
from dependencies import verify_password,findOne
from schemas import RegistrationForm
load_dotenv()


server = Flask(__name__)
database_connection_string = os.environ.get("DATABASE_CONNECTION")
connection = psycopg2.connect(database_connection_string)


fake_database = [{"username":"Michael",
                "password":"hashedPassword##"}]


@server.route("/login",methods = ['GET','POST'])
def login():
    #check whether user passed in the required auth details
    if not request.authorization:
        response = jsonify(status_code = 401,
                        detail = "Unauthorized Credentials",
                        mimetype='application/json')
        return response
    
    #if auth is not None
    username = request.authorization.username
    password = request.authorization.password

    #get password from db (fake db dictionary in this case)

    user = findOne(fake_database,condition = username)
    if  user is None:
        response = jsonify(status_code = 404,
            detail = "User Not Found",
            mimetype='application/json')

    verify_password(password,list[user][0]['password'])
    return f"<p>Hello {auth}</p>"


@server.route("/register",methods = ['POST'])
def register():
    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        
        if valid_login(request.form['username'],
                       request.form['password']):

            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


if __name__ == "__main__":
    server.run(debug = True)
