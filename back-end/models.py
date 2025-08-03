from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company= db.Column(db.String(100),nullable=False)
    location= db.Column(db.String(100))
    date_posted = db.Column(db.Date)
    url= db.Column(db.String(200))
    applied = db.Column(db.Boolean, default=False)

def __repr__(jobseeker):
    return f"<Job {jobseeker.title} at {jobseeker.company}>"
