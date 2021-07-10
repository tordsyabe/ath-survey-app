from athsurveyapp import db


class Employee(db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    designation = db.Column(db.String, nullable=False)
    branch_id = db.relationship(db.Integer, db.ForeignKey('employee.id'))

    def __init__(self, name, code, designation):
        self.name = name
        self.code = code
        self.designation = designation
