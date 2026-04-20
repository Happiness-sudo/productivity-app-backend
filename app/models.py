from . import db, bcrypt

# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    notes = db.relationship('Note', backref='user', lazy=True)

    # PASSWORD SETTER
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # PASSWORD CHECKER
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


# NOTE MODEL (RESOURCE)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(300))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)