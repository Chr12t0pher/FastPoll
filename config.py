from os import path, environ

WTF_CSRF_ENABLED = True

if environ.get("SECRET_KEY") is None:
    SECRET_KEY = "123CHANGEME"
else:
    SECRET_KEY = environ["SECRET_KEY"]

if environ.get("FASTPOLL_MYSQL") is None:
    basedir = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "database.db")
    SQLALCHEMY_MIGRATE_REPO = path.join(basedir, "db_repo")
else:
    SQLALCHEMY_DATABASE_URI = environ["FASTPOLL_MYSQL"]