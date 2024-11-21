from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json
import pytz
from datetime import datetime, timedelta


# define a blueprint for views
# means we have a collection of routes/urls that are related to each other
# allows us to organize these in separate files
views = Blueprint('views', __name__)

# define a route for home page
@views.route('/', methods=['GET', 'POST']) # defines url to where this next function takes us (function runs when we go to this url)
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Request too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Injury added!', category='success')
    
    est = pytz.timezone('US/Eastern')
    for note in current_user.notes:
        if note.date.tzinfo is None:
            # Make the datetime object timezone-aware
            note.date = pytz.utc.localize(note.date)
        # Convert to EST
        note.date = note.date.astimezone(est)


    return render_template("home.html", user=current_user) #renders the html inside of home.html

@views.route('/trainerHome', methods=['GET', 'POST']) # defines url to where this next function takes us (function runs when we go to this url)
@login_required
def trainerHome():
    notes = Note.query.all()
    users = User.query.all()
    user_dict = {user.id: user.first_name + " " + user.last_name for user in users}
    est = pytz.timezone('US/Eastern')

    current_time = datetime.now()
    current_time = pytz.utc.localize(current_time)
    time_plus_5_hours = timedelta(hours=5)
    notes_with_diff = {}

    for note in notes:
        if note.date.tzinfo is None:
            # Make the datetime object timezone-aware
            note.date = pytz.utc.localize(note.date)
        # Convert to EST
        note.date = note.date.astimezone(est)

        time_diff = current_time - note.date + time_plus_5_hours
        days = time_diff.days
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds % 3600) // 60
        notes_with_diff[note] = [days, hours, minutes]


    return render_template("trainerHome.html", user=current_user, notes=notes, diffs=notes_with_diff, user_dict = user_dict) #renders the html inside of trainerHome.html

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id or current_user.role == "trainer":
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

@views.route('/trainer-accept', methods=['POST'])
def trainer_accept():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if current_user.role == "trainer":
            note.trainer_assigned = current_user.first_name + " " + current_user.last_name
            note.status = "accepted"
            db.session.commit()
            
    return jsonify({})

