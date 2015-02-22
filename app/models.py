from app import db
from json import loads


class Poll(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    options = db.Column(db.String)  # List of values in JSON.
    votes = db.Column(db.String)  # Number of votes for each option in JSON.

    def load_options(self):
        return loads(self.options)

    def load_votes(self):
        return loads(self.votes)