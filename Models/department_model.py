from . import db
class Department(db.Model):
	__tablename__= 'departments'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	parentID = db.Column(db.Integer, nullable=True)
	clubs = db.relationship('Club', backref = db.backref("DepartmentOfClubs"))
	eligibilities = db.relationship('Eligibility', backref = db.backref("DepartmentOfEligibilities"))
	events = db.relationship('Event', backref = db.backref("DepartmentOfEvents"))

	def __repr__(self):
		return '<Department %r>' % self.id
