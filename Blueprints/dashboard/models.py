from extensions import db
from datetime import datetime
from auth.models import Teacher, Student, Admin


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    student_id = db.Column(
        db.Integer, db.ForeignKey('student.id'), nullable=True)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(50))
    subject_code = db.Column(db.String(50))
    student_marks = db.Column(db.Numeric, nullable=False)
    exam_pass_marks = db.Column(db.Numeric, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    # Exam + Student [m:m]
    student_link = db.relationship("StudentExam", back_populates="exams")


class StudentExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Exam + Student [m:m]
    exams = db.relationship(
        "Exam", back_populates="student_link", uselist=True)
    student_ = db.relationship(
        "Student", back_populates="exam_link", uselist=True)



