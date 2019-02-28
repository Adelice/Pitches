from flask import render_template,request,redirect,url_for,abort
from ..models import  User, Pitch,Comment
from . import main
from .forms import UpdateProfile,CommentForm,AddPitchForm
from ..import db,photos
from flask_login import login_required
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

   
    title = 'Home - Welcome to Pitches'
    search_pitches=Pitch.get_pitches()


    return render_template('index.html', title = title,pitches=search_pitches )


@main.route('pitch/new', methods = ['GET','POST'])
@login_required
def add_pitch():
    form = AddPitchForm()
   
    if form.validate_on_submit():
       category = form.category.data
       pitch = form.content.data
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        return redirect(url_for('main.movie',movie_id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))