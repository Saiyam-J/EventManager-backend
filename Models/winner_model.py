from . import db
class Winner(db.Model):
	__tablename__= 'winners'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
	teamID = db.Column(db.Integer, nullable=True)
	position = db.Column(db.Integer, nullable=False)
	teamname = db.Column(db.String(250), nullable=True)

	def __repr__(self):
		return '<Winner %r>' % self.id
