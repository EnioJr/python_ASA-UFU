import os.path
basedir = os.path.abspath(os.path.dirname("/home/windysson/flask/app/"))
DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "storage.db")
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "99609182"