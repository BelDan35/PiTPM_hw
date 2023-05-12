from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:PiTPM_12_05_23/lesson_14/sqlite_python.db'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'


post_tags = db.Table('post_tags',
        db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
        db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
    )

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow(), onupdate=datetime.utcnow())
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))

    def __repr__(self):
        return "<{}:{}>".format(self.id,  self.title[:10])

class Category(db.Model):

    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow())
    posts = db.relationship('Post', backref='category')

    def __repr__(self):
        return "<{}:{}>".format(id, self.name)
    
class  Tag(db.Model):

    __tablename__ = 'tags'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_on  =  db.Column(db.DateTime(), default=datetime.utcnow())
    posts = db.relationship('Post', secondary=post_tags, backref='tags')

    def __repr__(self):
        return "<{}:{}>".format(id, self.name)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    designation = db.Column(db.String(255), nullable=False)
    doj = db.Column(db.Date(), nullable=False)
    dl = db.relationship('DriverLicense', backref='employee', uselist=False)

class DriverLicense(db.Model):
    __tablename__ = 'driverlicense'
    id = db.Column(db.Integer(), primary_key=True)
    license_number = db.Column(db.String(255), nullable=False)
    renewed_on = db.Column(db.Date(), nullable=False)
    expiry_date = db.Column(db.Date(), nullable=False)
    employee_id = db.Column(db.Integer(), db.ForeignKey('employees.id'))  # Foreign key

app.run()