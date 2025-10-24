from extensions import db
from datetime import datetime



class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    # FK => ValidTeacher
    valid_teacher_id = db.Column(db.Integer,db.ForeignKey("validteacher.id"), unique=True, nullable=True)

    # Teacher+ValidTeacher [1:1]
    valid_teacher = db.relationship("ValidTeacher", back_populates="teacher", uselist=False)

  


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    admin_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)

    # FK => ValidStudent
    valid_student_id = db.Column(db.Integer,db.ForeignKey("validstudent.id"), unique=True, nullable=True)

    # Admin+ValidStudent [1:1]
    valid_admin_student = db.relationship("ValidStudent", back_populates="admin", uselist=False)


class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)    
    student_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow) 

    # FK => ValidStudent
    valid_student_id = db.Column(db.Integer,db.ForeignKey("validstudent.id"), unique=True, nullable=True) 

    # Student+ValidStudent [1:1]
    valid_student = db.relationship("ValidStudent", back_populates="student", uselist=False)  

    # Exam + Student
    exam_link = db.relationship("StudentExam", back_populates="student_", uselist=True)
