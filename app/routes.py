import os
from app import app
from flask import render_template, request, redirect

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://MrHypeman:tWHNmGVrmDVacOuA@cluster0-7hbc1.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
@app.route('/')
@app.route('/index')
def index():
    #connect to the Mongo DB
    collection = mongo.db.events
    #find all of the events in that database using a query , store it as events
    #{} will return everything in the database
    #list constructor will turn the results into a list (of dictionaries/objects)
    events = list(collection.find({}))
    return render_template('index.html', events = events)
# INDEX




# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": "test", "event date": "today"})
    # return a message to the user
    return "you added a thing to the thing, go look at the thing"

# Add this route to the routes.py page

# need a get and a post method
@app.route('/results', methods = ["get", "post"])
def results():
    # store userinfo from the form
    user_info = dict(request.form)
    print(user_info)
    #store the event_name
    event_name = user_info["event_name"]
    print("the event name is ", event_name)
    #store the event_date
    event_date = user_info["event_date"]
    print("the event date is ", event_date)
    #store the catagory
    catagory = user_info["catagory"]
    print("The catagory is" , catagory)
    #connect to Mongo DB
    collection = mongo.db.events
    #insert the user's input event_name and event_date to MONGO
    collection.insert({"event_name": event_name, "event_date": event_date, "catagory": catagory})
    #(so that it will continue to exist after this program stops)
    #redirect back to the index page
    return redirect('/index')

@app.route('/delete_all')
def delete_all():
    #connect to mongo data database
    collection = mongo.db.events
    #delete everything
    collection.delete_many({})
    #redirect back tot the index page
    return redirect('/index')

@app.route('/filter_school')
def filter_school():
    collection = mongo.db.events
    events = list(collection.find({"catagory": "school"}))
    print(events)
    return render_template('filter_school.html', events = events)

@app.route('/filter_personal')
def filter_personal():
    collection = mongo.db.events
    events = list(collection.find({"catagory": "personal"}))
    print(events)
    return render_template('filter_personal.html', events = events)

@app.route('/filter_dates')
def filter_dates():
    collection = mongo.db.events
    events = list(collection.find({"catagory": "dates"}))
    print(events)
    return render_template('filter_dates.html', events = events)

@app.route('/filter_food')
def filter_food():
    collection = mongo.db.events
    events = list(collection.find({"catagory": "food"}))
    print(events)
    return render_template('filter_food.html', events = events)

    
