from flask import render_template,request,redirect,url_for,abort
from ..models import  User, Pitch,Comment,PhotoProfile
from . import main
from .forms import UpdateProfile,AddPitchForm,CommentForm
from ..import db,photos
from flask_login import login_required,current_user
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

   
    title = 'Home - Welcome to Pitches'
    search_pitches=Pitch.get_pitches()


    return render_template('index.html', title = title,pitches=search_pitches )


@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def add_pitch():
    form = AddPitchForm()
   
    if form.validate_on_submit():
       category = form.category.data
       content = form.content.data

       new_pitch=Pitch(description=content,category=category, user=current_user)
       new_pitch.save_pitch()

       return redirect(url_for('main.index'))
    search_pitches = Pitch.query.all()
    title = 'Please add your pitch'
    return render_template('pitches.html' , title = title,pitch_form=form )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
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
@main.route('/new/comment/<int:id>' , methods = ['GET', 'POST'])
@login_required
def add_comment(id):
    pitch=Pitch.query.filter_by(id=id).first()
    if pitch is None:
        abort(404)
    form=CommentForm()
    if form.validate_on_submit():
        comment=form.comment.data 
        new_comment=Comment(content=comment , pitch=pitch, user=current_user)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('comment.html',comment_form=form) 
@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch=Pitch.query.filter_by(id=id).first()
    comments=Comment.get_comment(id=id)
    return render_template('pitch.html',pitch=pitch,comments=comments)

