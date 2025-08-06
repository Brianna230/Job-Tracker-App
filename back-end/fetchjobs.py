import requests, json
from flask import Flask
from models import db , Job
import os
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)

def fetch_jobs():
 url = "https://jsearch.p.rapidapi.com/search"

 for page in range(1,21):
  querystring ={"query":" entry level IT jobs in new york","page":str(page),"num_pages":"1","country":"us","date_posted":"all"}

 headers ={
    "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
 }

 response = requests.get(url, headers=headers,params=querystring)

 jobs=[]
 
 if response.status_code == 200:
  data = response.json()    # formatted the data in json formatted
  jobs = data.get('data',[]) # get all data so the user can run it in terminal
 else:
    print(f"Failed to retrieve  data{response.status_code}")


 with app.app_context():
  for job in jobs:
    title= job.get('job_title','N/A')
    company = job.get('employer_name','N/A')
    location = job.get('job_city', 'N/A')
    apply_link = job.get('job_apply_link','N/A')
    print(f"Title:{title} | Company:{company} | Location:{location} | Apply Link:{apply_link}")
    existing_job = Job.query.filter_by(apply_link=apply_link).first()
    if not existing_job:
     new_job = Job(
      title = title,
      company=company,
      location=location,
      apply_link=apply_link,
      applied=False
     )
     db.session.add(new_job)
     db.session.commit()

 print("Job fetch complete.\n")

# fetch_jobs()




schedule.every(10).seconds.do(fetch_jobs)
while True:
  schedule.run_pending()
  time.sleep(5)
