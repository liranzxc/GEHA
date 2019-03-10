from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rkPfWbFHQQ:uCispJwgzm@remotemysql.com/rkPfWbFHQQ'


#'sqlite:////test.db'
#'mysql://rkPfWbFHQQ:uCispJwgzm@remotemysql.com/rkPfWbFHQQ'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all() # In case user table doesn't exists already. Else remove it.    

#admin = User('admin', 'admin@example.com')

# admin = User('admin', 'admin@example.com')

# user1 = User('user1', 'u1@example.com')
# user2 = User('user2', 'u2@example.com')

user2 = User('user5', 'u332@example.com')
db.session.add(user2)

db.session.commit() # This is needed to write the changes to database


#db.session.add(admin)

#db.session.commit() # This is needed to write the changes to database

print(User.query.all())

print(User.query.filter_by(email='admin@example.com').first())