from . import db
class Eligibility(db.Model):
	__tablename__= 'eligibilities'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	events = db.relationship('Event', backref = db.backref("EligibilityOfEvents"))

	def __repr__(self):
		return '<Eligibility %r>' % self.id
