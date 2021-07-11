from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(
        timezone=True), onupdate=func.now())
    designation = db.Column(db.String, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey(
        'branch.id'), nullable=False)

    def __init__(self, name, code, designation):
        self.name = name
        self.code = code
        self.designation = designation


class Branch(db.Model):

    __tablename__ = "branch"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime(
        timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(
        timezone=True), onupdate=func.now())
    address = db.Column(db.String())
    employees = db.relationship('Employee', backref='branch', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address
