
from extensions import db
from auth.models import Teacher,Admin,Student



class CompulsarySubject(db.Model):
    __tablename__ = "compulsarysubject"

    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(50),unique=True)
    subject_code = db.Column(db.String(50),unique=True)

    # Class+ClassCompulsarySubject [m:m]
    class_link = db.relationship("ClassCompulsarySubject",back_populates="compulsary_subject")

    def __repr__(self):
        return f"<CompulsarySubject: {self.subject_code} - {self.subject_name}>"
    



class OptionalSubject(db.Model):
    __tablename__ = "optionalsubject"
    

    id = db.Column(db.Integer,primary_key=True)
    subject_name = db.Column(db.String(50),unique=True)
    subject_code = db.Column(db.String(50),unique=True)


    # FK => Class id
    class_id = db.Column(db.Integer,db.ForeignKey("class.id"))
    
    # Class+OptionalSubject [1:m]
    class_ = db.relationship("Class", back_populates="optional_subjects")

    def __repr__(self):
        return f"<OptionalSubject: {self.subject_code} - {self.subject_name}>"


class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer,primary_key=True) 
    class_name = db.Column(db.String(50),unique=True,nullable=False)

    # Class+ClassTeacher [m:m]
    valid_teacher_links = db.relationship("ClassTeacher", back_populates="class_")

    # Class+Student [1:m]
    students = db.relationship("ValidStudent", back_populates="class_", uselist=True)

    # Class+OptionalSubject [1:m]
    optional_subjects = db.relationship("OptionalSubject", back_populates="class_", uselist=True)

    # Class+ClassCompulsarySubject [m:m]
    compulsary_subjects = db.relationship("ClassCompulsarySubject",back_populates="class_link")

    def __repr__(self):
        return f"<Class: {self.class_name}>"
    

class ClassCompulsarySubject(db.Model):
    __tablename__ = "classcompulsarysubject"

    id = db.Column(db.Integer,primary_key=True) 
    class_id = db.Column(db.Integer,db.ForeignKey("class.id"))
    compulsary_subject_id = db.Column(db.Integer,db.ForeignKey("compulsarysubject.id"))

    # [m:m]
    class_link = db.relationship("Class", back_populates="compulsary_subjects")
    compulsary_subject = db.relationship("CompulsarySubject", back_populates="class_link")

    def __repr__(self):
        return f"<ClassCompulsarySubject: {self.class_link.class_name} - {self.compulsary_subject.subject_name}>"
    





class ValidTeacher(db.Model):
    __tablename__ = "validteacher"

    id = db.Column(db.Integer,primary_key=True) 
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)

    # ValidTeacher+ClassTeacher [m:m]
    class_links = db.relationship("ClassTeacher", back_populates="valid_teacher")

     # Teacher+ValidTeacher [1:1] 
    teacher = db.relationship("Teacher", back_populates="valid_teacher", uselist=False)

    def __repr__(self):
        return f"<ValidTeacher: {self.first_name} {self.last_name}>"




class ClassTeacher(db.Model):
    __tablename__ = "classteacher"

    id = db.Column(db.Integer,primary_key=True) 
    class_id = db.Column(db.Integer,db.ForeignKey("class.id"))
    valid_teacher_id = db.Column(db.Integer,db.ForeignKey("validteacher.id"))

     
    class_ = db.relationship("Class", back_populates="valid_teacher_links")
    valid_teacher = db.relationship("ValidTeacher", back_populates="class_links")

    def __repr__(self):
        return f"<ClassTeacher: {self.class_.class_name} - {self.valid_teacher.first_name} {self.valid_teacher.last_name}>"




class ValidStudent(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)   

    # Class+ValidStudent [1:m]
    class_id = db.Column(db.Integer, db.ForeignKey("class.id"))

    class_ = db.relationship("Class",back_populates="students")

    # Admin+ValidStudent [1:1]
    admin = db.relationship("Admin", back_populates="valid_admin_student", uselist=False)

    # Student+ValidStudent [1:1]
    student = db.relationship("Student", back_populates="valid_student", uselist=False)  

    def __repr__(self):
        return f"<ValidStudent: {self.first_name} {self.last_name}>"

