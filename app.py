from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import os
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_NAME'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from Models.category_model import Category
from Models.club_model import Club
from Models.department_model import Department
from Models.eligibility_model import Eligibility
from Models.event_category_model import Event_category
from Models.event_model import Event
from Models.winner_model import Winner
from datetime import datetime

@app.route("/")
def home():
	return {"success":"true"}

@app.route("/categories", methods=['GET'])
def categories():
	categories = Category.query.all()
	response = {}
	response['categories'] = []
	for category in categories:
		response['categories'].append({"name": category.name, "id": category.id})
	return response

@app.route("/clubs", methods=['GET'])
def clubs():
	clubs = Club.query.all()
	response = {}
	response['clubs'] = []
	for club in clubs:
		clubinfo = {}
		clubinfo['name'] = club.name
		clubinfo['id'] = club.id
		clubinfo['department_id'] = club.department_id
		clubinfo['members'] = club.members
		clubinfo['logo'] = club.logo
		clubinfo['join_link'] = club.join_link
		clubinfo['description'] = club.description
		clubinfo['uuid'] = club.uuid
		response['clubs'].append(clubinfo)
	return response

@app.route("/departments", methods=['GET'])
def departments():
	departments = Department.query.all()
	response = {}
	response['departments'] = []
	for department in departments:
		if department.parentID is None:
			departmentinfo = {}
			departmentinfo['name'] = department.name
			departmentinfo['id'] = department.id
			response['departments'].append(departmentinfo)
		else:
			for dep in response['departments']:
				if dep['id'] == department.parentID:
					if 'subdepartments' not in dep:
						dep['subdepartments'] = []
					dep['subdepartments'].append({"name":department.name, "id":department.id})
	return response

@app.route("/club/<string:club_uid>")
def club(club_uid):
	club = Club.query.filter_by(uuid=club_uid).first()
	response = {}

@app.route("/upcoming")
def upcoming():
	events = Event.query.filter(Event.startdatetime > datetime.now()).all()
	print(events)
	response = {}
	response['events'] = []
	for event in events:
		eventinfo = {}
		eventinfo["name"] = event.name
		eventinfo["uuid"] = event.uuid
		eventinfo["startdatetime"] = event.startdatetime
		eventinfo["enddatetime"] = event.enddatetime
		eventinfo["description"] = event.description
		eventinfo["venue"] = event.venue
		eventinfo["club_id"] = event.club_id
		eventinfo["eligibility_id"] = event.eligibility_id
		eventinfo["department_id"] = event.department_id
		eventinfo["reg_link"] = event.reg_link
		eventinfo["poster"] = event.poster
		eventinfo["isCompleted"] = event.isCompleted
		categories = []
		for event_category in event.event_categories:
			category = Category.query.filter_by(id=event_category.category_id).first()
			categories.append({"name": category.name, "id": category.id})
		eventinfo["categories"] = categories
		response['events'].append(eventinfo)
	return response

@app.route("/event/<string:event_uid>")
def event(event_uid):
	event = Event.query.filter_by(uuid=event_uid).first()
	response = {}
	response["name"] = event.name
	response["uuid"] = event.uuid
	response["startdatetime"] = event.startdatetime
	response["enddatetime"] = event.enddatetime
	response["description"] = event.description
	response["venue"] = event.venue
	response["club_id"] = event.club_id
	response["eligibility_id"] = event.eligibility_id
	response["department_id"] = event.department_id
	response["reg_link"] = event.reg_link
	response["poster"] = event.poster
	response["isCompleted"] = event.isCompleted
	categories = []
	for event_category in event.event_categories:
		category = Category.query.filter_by(id=event_category.category_id).first()
		categories.append({"name": category.name, "id": category.id})
	response["categories"] = categories

	return response



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)