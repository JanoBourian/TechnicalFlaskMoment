from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db
from . import login_manager

## Functions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## Models
class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role {self.name}>"


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    
    @property
    def password(self):
        raise AttributeError("Password is not readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_confirmation_token(self):
        s = Serializer(current_app.config["SECRET_KEY"])
        return s.dumps({'confirm': self.id})
    
    def confirm(self, token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        
        if data.get("confirm") != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return f"<User {self.username}>"
