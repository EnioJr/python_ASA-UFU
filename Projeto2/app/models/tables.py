from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
        
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Users %r>" % self.username

class Command(db.Model):

    __tablename__ = "commands"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    command = db.Column(db.Text)

    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, data, user_id, command):
        self.data = data
        self.user_id = user_id
        self.command = command

    def __repr__(self):
        return "<Command %r>" % self.id
