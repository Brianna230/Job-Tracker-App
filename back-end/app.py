from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db, Job
# from fetchjobs import fetch_jobs
from flask_cors import CORS
import os
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)

with app.app_context():
    db.create_all()

def fetch_latest_job():
    jobs = Job.query.order_by(Job.id.asc()).limit(21).all() 
    return[job.to_dict() for job in jobs]

@app.route("/", methods=['GET'])
def get_latest_job():
    job_data = fetch_latest_job()
    return jsonify(job_data)




if __name__ == "__main__":
    app.run(debug=True)