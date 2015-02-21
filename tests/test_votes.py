from app import db
from app.models import Poll
from json import loads, dumps
from random import choice as randchoice

options = ["Option 1", "Option 2", "Option 3"]
x = 0

while x < 300:
    x += 1
    current_poll = Poll.query.filter_by(id="2710981503423824268").first()
    current_votes = loads(current_poll.votes)
    current_votes[randchoice(options)] += 1
    current_poll.votes = dumps(current_votes)
    db.session.add(current_poll)
    db.session.commit()