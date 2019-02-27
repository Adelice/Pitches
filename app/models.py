from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

       



class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255)) 
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

   
    
    def __repr__(self):
        return f'User {self.username}'
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))   

class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    description=db.Column(db.String(255))
    category=db.Column(db.String(255))
    comments= db.relationship('Comment',backref = 'comment',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'
    pass_secure  = db.Column(db.String(255))

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer, db.ForeignKey("pitch.id"))
    content=db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'

# class PhotoProfile(db.Model):
#     __tablename__ = 'profile_photos'

#     id = db.Column(db.Integer,primary_key = True)
#     pic_path = db.Column(db.String())
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

