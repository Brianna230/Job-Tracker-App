from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company= db.Column(db.String(100),nullable=False)
    location= db.Column(db.String(100))
    date_posted = db.Column(db.Date)
    apply_link= db.Column(db.String(500))
    applied = db.Column(db.Boolean, default=False)

    def to_dict(self):  #This help show the data from the databse to show in the browser thought flask.
        return{
            "id": self.id,
            "title": self.title,
            "company":self.company,
            "location": self.location,
            "date_posted": self.date_posted,
            "apply_link": self.apply_link,
            "applied": self.applied

        }
    


def __repr__(jobseeker):
    return f"<Job {jobseeker.title} at {jobseeker.company}>"
