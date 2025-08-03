from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db
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
def index():
    return jsonify({"Jobs":["Software Apprentice","Junior Developer"]})

if __name__ == "__main__":
    app.run(debug=True)