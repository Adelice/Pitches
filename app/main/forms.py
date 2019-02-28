from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):
    comment = TextAreaField('Pitch comment' , validators=[Required()])
    submit = SubmitField('submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 
class AddPitchForm(FlaskForm):
    category= SelectField('Category:',choices=[('pickup-lines' , 'Pickup Lines'),('Interview-pitch' ,'Interview Pitch'),('Promotion-pitch' , 'Promotion Pitch')]) 
    content = TextAreaField('Pitch', validators = [Required])  
    submit = SubmitField('SUBMIT')                                      