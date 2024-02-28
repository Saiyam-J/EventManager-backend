from . import db
class Event(db.Model):
	__tablename__= 'events'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	poster = db.Column(db.String(100), nullable=True)
	description = db.Column(db.String, nullable=False)
	reg_link = db.Column(db.String(250), nullable=False)
	venue = db.Column(db.String(250), nullable=False)
	startdatetime = db.Column(db.DateTime, nullable=False)
	enddatetime = db.Column(db.DateTime, nullable=False)
	club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
	eligibility_id = db.Column(db.Integer, db.ForeignKey('eligibilities.id'))
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	uuid = db.Column(db.String(36), nullable=False)
	event_categories = db.relationship('Event_category', backref = db.backref("EventOfEvent_categories"))
	winners = db.relationship('Winner', backref = db.backref("EventOfWinners"))

	def __repr__(self):
		return '<Event %r>' % self.id
