from datetime import datetime
from extensions import db
from flask_login import UserMixin



class CompulsarySubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(50),unique=True)
    subject_code = db.Column(db.String(50),unique=True)
    



class OptionalSubject(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(50),unique=True)
    subject_code = db.Column(db.String(50),unique=True)
    


class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer,primary_key=True) 
    class_name = db.Column(db.String(50),unique=True,nullable=False)

    # Class+ClassTeacher
    valid_teacher_links = db.relationship("ClassTeacher", back_populates="class_")

    def __repr__(self):
        return f"<Class {self.class_name}>"



class ValidTeacher(db.Model):
    __tablename__ = "validteacher"

    id = db.Column(db.Integer,primary_key=True) 
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)

    # ValidTeacher+ClassTeacher
    class_links = db.relationship("ClassTeacher", back_populates="valid_teacher")

    def __repr__(self):
        return f"<ValidTeacher {self.first_name} {self.last_name}>"




class ClassTeacher(db.Model):
    __tablename__ = "classteacher"

    id = db.Column(db.Integer,primary_key=True) 
    class_id = db.Column( db.Integer,db.ForeignKey("class.id"))
    valid_teacher_id = db.Column(db.Integer,db.ForeignKey("validteacher.id"))


    class_ = db.relationship("Class", back_populates="valid_teacher_links")
    valid_teacher = db.relationship("ValidTeacher", back_populates="class_links")

    def __repr__(self):
        return f"<ClassTeacher {self.class_.class_name} - {self.valid_teacher.first_name} {self.valid_teacher.last_name}>"




class ValidStudent(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)    

