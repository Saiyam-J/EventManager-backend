from . import db
class Category(db.Model):
	__tablename__= 'categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	event_categories = db.relationship('Event_category', backref = db.backref("CategoryOfEvent_categories"))

	def __repr__(self):
		return '<Category %r>' % self.id
