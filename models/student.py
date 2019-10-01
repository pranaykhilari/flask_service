from app import db


class Student(db.Model):
    __tablename = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone_num = db.Column(db.String(128))

