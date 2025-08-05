import requests, json
import os
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

def fetch_jobs():
 url = "https://jsearch.p.rapidapi.com/search"

 querystring ={"query":" entry level IT jobs in new york","page":"1","num_pages":"1","country":"us","date_posted":"all"}

 headers ={
    "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
 }

 response = requests.get(url, headers=headers,params=querystring)

 

 if response.status_code == 200:
  data = response.json()    # formatted the data in json formatted
  jobs = data.get('data',[]) # get all data so the user can run it in terminal

   

  for job in jobs:
    title= job.get('job_title','N/A')
    company = job.get('employer_name','N/A')
    location = job.get('job_city', 'N/A')
    applylink = job.get('job_apply_link','N/A')
    print(f"Title:{title} | Company:{company} | Location:{location} | Apply Link:{applylink}")
 else:
   print(f"Failed to retrieve  data{response.status_code}")

 

fetch_jobs()




schedule.every(10).minutes.do(fetch_jobs)
while True:
  schedule.run_pending()
  time.sleep(1)
