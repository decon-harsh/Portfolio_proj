#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

#app configurations
app.config['SECRET_KEY']='S\x821\x84\xdeG@\xed<- _\xa5\xfb\x91\xb8s\xae\xad\x9d\x9a:H\xaa'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)



from Profile import routes