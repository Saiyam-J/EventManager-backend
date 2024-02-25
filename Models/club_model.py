from . import db
class Club(db.Model):
	__tablename__= 'clubs'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	members = db.Column(db.Integer, nullable=True)
	logo = db.Column(db.String(250), nullable=False)
	join_link = db.Column(db.String(250), nullable=True)
	description = db.Column(db.String, nullable=False)
	uuid = db.Column(db.String(36), nullable=False)
	events = db.relationship('Event', backref = db.backref("ClubOfEvents"))

	def __repr__(self):
		return '<Club %r>' % self.id
