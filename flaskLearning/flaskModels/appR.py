from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import os 

app = Flask(__name__)

# Database configuration

#defines the location of the database file and disables the modification tracking feature of SQLAlchemy, 
# which can help improve performance.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize the database

db = SQLAlchemy(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

#defining a model which represents a table inside of our database 

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    event = db.Column(db.String(200), nullable=False)

    #id: aut incrementing primary key 
    #date: stores event timestamps, default to the current time 
    #event: stores the event description which cannot be null

#creating the database 

with app.app_context():
    db.create_all()

#inserting new data into the database 
#to add events you create an event instance and commit it

def add_event(event_description):
    new_event = Event(event=event_description)
    db.session.add(new_event)
    db.session.commit()

#querying the database 

#db.session is used to fetch and store data 

#GET: fetches all events and displays them,
#POST: ADDS a new event to the database 

@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        db.session.add(Event(date=datetime.datetime.now().__str__(), event=request.form['eventBox']))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', eventsList=db.session.execute(db.select(Event).order_by(Event.date)).scalars())
    
    