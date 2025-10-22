from extensions import db 
from datetime import datetime
from schooladmin.models import * 


class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)    
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)    