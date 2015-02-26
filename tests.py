import unittest
import uuid
from json import dumps
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

    def test_isOnline(self):
        assert "FastPoll" in str(self.app.get("").data)  # The site loads successfully.

    def test_newPoll(self):
        new_poll = Poll(id=str(uuid.uuid4().int >> 64),
                        title="Title",
                        desc="Description",
                        options=dumps(["Option 1", "Option 2"]),
                        votes=dumps([]),
                        voters=dumps([]),
                        public=False,
                        ip=True)
        db.session.add(new_poll)
        db.session.commit()
        assert Poll.query.filter_by(title="Title").first() is not None  # We can add Polls to a database.


if __name__ == "__main__":
    unittest.main()