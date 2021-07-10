from athsurveyapp import db


class Branch(db.Model):

    __tablename__ = "branch"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    employees = db.relationship('Employee', backref='branch', lazy=True)
