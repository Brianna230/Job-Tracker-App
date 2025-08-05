from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db
from fetchjobs import fetch_jobs
from flask_cors import CORS
import os
load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/api/jobs', methods=['GET'])
def get_latest_job():
    jobs = fetch_jobs()
    return(jsonify(jobs))

if __name__ == "__main__":
    app.run(debug=True)