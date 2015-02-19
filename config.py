from os import path

WTF_CSRF_ENABLED = True
SECRET_KEY = "8a7c5c62e3dd7ba27aa280e8d37055e5953ca35881883875c83810b791dc533c"

basedir = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(basedir, "database.db")
SQLALCHEMY_MIGRATE_REPO = path.join(basedir, "db_repo")