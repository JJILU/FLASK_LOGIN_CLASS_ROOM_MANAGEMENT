from extensions import db 
from datetime import datetime

schoolclass_compulserysubject = db.Table(
    'schoolclass_compulserysubject',
    db.Column('schoolclass_id', db.Integer,db.Foreignkey('schoolclass.id')),
    db.Column('compulserysubject_id', db.Integer,db.Foreignkey('compulserysubject.id'))
)

class SchoolClass(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    class_name = db.Column(db.String(40),unique=True,nullable=False)

    


class CompulserySubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(80),unique=True,nullable=False)
    subject_code = db.Column(db.String(80),unique=True,nullable=False)

class OptionSubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(80),unique=True,nullable=False)
    subject_code = db.Column(db.String(80),unique=True,nullable=False)    
    

class EmployeedTeacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40),nullable=False)
    last_name = db.Column(db.String(40),nullable=False)

    # one-to-one relationship with Teacher model
    teacher = db.relationship('Teacher',backref='employed_teacher', uselist=False)


class RegisteredStudents(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40),nullable=False)
    last_name = db.Column(db.String(40),nullable=False)
    class_id = db.Column()

    # one-to-one relationship with Student model
    student = db.relationship('Student',backref='registered_student', uselist=False)  





class Teacher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    teacher_school_id = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,onupdate=datetime.utcnow)
    employed_teacher = db.relationship('EmployeedTeacher',backref='teacher', uselist=False)
    employed_teacher_id = db.Column(db.Integer,db.ForeignKey('employedteacher.id'))
    


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)




class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)        