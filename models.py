from config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
#     # password = db.Column(db.String(50), nullable=False)
#     entries = db.relationship("JournalEntry", backref="author")


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    # date = db.Column(db.DateTime, nullable=False)
    # author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
