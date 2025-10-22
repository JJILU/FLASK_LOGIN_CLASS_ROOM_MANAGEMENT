from extensions import db 
from datetime import datetime
from schooladmin.models import ValidStudent,ValidTeacher


class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    # FK => ValidTeacher
    valid_teacher_id = db.Column(db.Integer,db.Foreign_Key("validteacher.id"))

    # Teacher+ValidTeacher [1:1]
    valid_teacher = db.relationship("ValidTeacher", back_populates="teacher", uselist=False)

  


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    # FK => ValidStudent
    valid_student_id = db.Column(db.Integer,db.Foreign_Key("validstudent.id"))

    # Admin+ValidStudent [1:1]
    valid_student = db.relationship("ValidStudent", back_populates="admin", uselist=False)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)    
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow) 

    # FK => ValidStudent
    valid_student_id = db.Column(db.Integer,db.Foreign_Key("validstudent.id")) 

    # Student+ValidStudent [1:1]
    valid_student = db.relationship("ValidStudent", back_populates="student", uselist=False)  