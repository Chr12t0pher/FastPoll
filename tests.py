import unittest
import uuid
from json import dumps, loads
from app import app, db
from app.models import Poll


class FastPollTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        cls.app = app.test_client()
        db.create_all()

    def test_Poll(self):
        new_poll = Poll(id=str(uuid.uuid4().int >> 64),
                        title="Title",
                        desc="Description",
                        options=dumps(["Option 1", "Option 2"]),
                        votes=dumps({"Option 1": 0, "Option 2": 0}),
                        voters=dumps([]),
                        public=False,
                        ip=True)
        db.session.add(new_poll)
        db.session.commit()
        assert Poll.query.filter_by(title="Title").first() is not None  # We can add Polls to a database.

        test_poll = Poll.query.first()
        test_poll.votes = loads(test_poll.votes)
        test_poll.votes["Option 1"] += 1
        test_poll.votes = dumps(test_poll.votes)
        db.session.add(test_poll)
        db.session.commit()
        assert loads(Poll.query.first().votes)["Option 1"] == 1  # We can get a Poll and vote on it.


if __name__ == "__main__":
    unittest.main()