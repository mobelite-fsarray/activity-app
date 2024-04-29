from flask import Flask
from app.pre_processing.category_cluster_model import extract_activity_tags
from app.authentification import login_user
from firebase_admin import firestore, auth

from flask import request

import uuid
import sklearn
import joblib

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def welcome():
    return "<p>Greeting folks!</p>"


@app.post("/login/")
def login():
    print(request.form)
    userRecord = login_user(request.form['username'],request.form['password'])
    return userRecord

@app.route("/<activityText>")
def getTags(activityText):
    return extract_activity_tags(activityText)

@app.route("/activity/<activityText>")
def addActivity(activityText):
    create_document('_activities', {'text': activityText,'tags':extract_activity_tags(activityText)})
    return extract_activity_tags(activityText)

@app.route("/activity/<activityText>")
def deleteActivity(id):
    delete_document('_activities', id)

@app.route("/activity/getCategories")
def getCategories():
    return extract_activity_tags(activityText)


