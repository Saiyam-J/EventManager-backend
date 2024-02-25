from . import db
class Event_category(db.Model):
	__tablename__= 'event_categories'
	id = db.Column(db.Integer, primary_key=True)
	event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

	def __repr__(self):
		return '<Event_category %r>' % self.id
