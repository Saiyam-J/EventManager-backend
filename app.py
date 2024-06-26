from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from flask_cors import CORS
import os
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost:3306/{}'.format(os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_NAME'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)
from Models.category_model import Category
from Models.club_model import Club
from Models.department_model import Department
from Models.eligibility_model import Eligibility
from Models.event_category_model import Event_category
from Models.event_model import Event
from Models.winner_model import Winner
from datetime import datetime, timedelta, date

@app.route("/api/")
def home():
	return {"success":"true"}

@app.route("/api/categories", methods=['GET'])
def categories():
	categories = Category.query.all()
	response = {}
	response['categories'] = []
	for category in categories:
		response['categories'].append({"name": category.name, "id": category.id})
	return response

@app.route("/api/clubs", methods=['GET'])
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

@app.route("/api/departments", methods=['GET'])
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

@app.route("/api/club/<string:club_uid>")
def club(club_uid):
	club = Club.query.filter_by(uuid=club_uid).first()
	response = {}

@app.route("/api/upcoming")
def upcoming():
	utc = datetime.now()
	indian = utc + timedelta(hours=5, minutes=30)
	events = Event.query.filter(Event.startdatetime > indian).all()
	response = {
        'events': [
            {
                'name': event.name,
                'uuid': event.uuid,
                'startdatetime': event.startdatetime,
                'enddatetime': event.enddatetime,
                'description': event.description,
                'venue': event.venue,
                'club_id': event.club_id,
                'eligibility_id': event.eligibility_id,
                'department_id': event.department_id,
                'reg_link': event.reg_link,
                'poster': event.poster,
                'categories': [{'name': category.name, 'id': category.id} for event_category in event.event_categories for category in Category.query.filter_by(id=event_category.category_id).all()]
            }
            for event in events
        ]
    }
	return response

@app.route("/api/event/<string:event_uid>")
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
	categories = []
	for event_category in event.event_categories:
		category = Category.query.filter_by(id=event_category.category_id).first()
		categories.append({"name": category.name, "id": category.id})
	response["categories"] = categories

	return response

@app.route("/api/eventson/<string:date>")
def eventon(date):
	from sqlalchemy import and_
	date = datetime.strptime(date, '%Y-%m-%d')
	events = Event.query.filter(and_(Event.startdatetime > date, Event.startdatetime < date + timedelta(days=1))).all()
	response = {
		'events': [
			{
				'name': event.name,
				'uuid': event.uuid,
				'startdatetime': event.startdatetime,
				'enddatetime': event.enddatetime,
				'description': event.description,
				'venue': event.venue,
				'club_id': event.club_id,
				'eligibility_id': event.eligibility_id,
				'department_id': event.department_id,
				'reg_link': event.reg_link,
				'poster': event.poster,
				'categories': [{'name': category.name, 'id': category.id} for event_category in event.event_categories for category in Category.query.filter_by(id=event_category.category_id).all()]
			}
			for event in events
		]
	}
	return response

@app.route("/api/eventsafter/<string:date>")
def eventafter(date):
	date = datetime.strptime(date, '%Y-%m-%d')
	events = Event.query.filter(Event.startdatetime > date).all()
	response = {
		'events': [
			{
				'name': event.name,
				'uuid': event.uuid,
				'startdatetime': event.startdatetime,
				'enddatetime': event.enddatetime,
				'description': event.description,
				'venue': event.venue,
				'club_id': event.club_id,
				'eligibility_id': event.eligibility_id,
				'department_id': event.department_id,
				'reg_link': event.reg_link,
				'poster': event.poster,
				'categories': [{'name': category.name, 'id': category.id} for event_category in event.event_categories for category in Category.query.filter_by(id=event_category.category_id).all()]
			}
			for event in events
		]
	}
	return response

@app.route("/api/eventsbetween/<string:startdate>/<string:enddate>")
def eventsbetween(startdate, enddate):
	from sqlalchemy import and_
	startdate = datetime.strptime(startdate, '%Y-%m-%d')
	enddate = datetime.strptime(enddate, '%Y-%m-%d')
	events = Event.query.filter(and_(Event.startdatetime > startdate, Event.startdatetime < enddate)).all()
	response = {
		'events': [
			{
				'name': event.name,
				'uuid': event.uuid,
				'startdatetime': event.startdatetime,
				'enddatetime': event.enddatetime,
				'description': event.description,
				'venue': event.venue,
				'club_id': event.club_id,
				'eligibility_id': event.eligibility_id,
				'department_id': event.department_id,
				'reg_link': event.reg_link,
				'poster': event.poster,
				'categories': [{'name': category.name, 'id': category.id} for event_category in event.event_categories for category in Category.query.filter_by(id=event_category.category_id).all()]
			}
			for event in events
		]
	}
	return response

@app.route("/api/eventsbefore/<string:date>")
def eventsbefore(date):
	date = datetime.strptime(date, '%Y-%m-%d')
	events = Event.query.filter(Event.startdatetime < date).all()
	response = {
		'events': [
			{
				'name': event.name,
				'uuid': event.uuid,
				'startdatetime': event.startdatetime,
				'enddatetime': event.enddatetime,
				'description': event.description,
				'venue': event.venue,
				'club_id': event.club_id,
				'eligibility_id': event.eligibility_id,
				'department_id': event.department_id,
				'reg_link': event.reg_link,
				'poster': event.poster,
				'categories': [{'name': category.name, 'id': category.id} for event_category in event.event_categories for category in Category.query.filter_by(id=event_category.category_id).all()]
			}
			for event in events
		]
	}
	return response



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=3000)