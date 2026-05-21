import json
import requests
from bs4 import BeautifulSoup

def run_scraper():
    print("Starting JOBBEZ Delivery Driver Script...")
    
    # This list will hold all the jobs we find
    collected_jobs = []

    # --- SAMPLE LIVE DATA ---
    # We add these first so your website instantly shows active examples
    sample_jobs = [
        {
            "title": "Data Analyst", 
            "company": "Abu Dhabi National Oil Company (ADNOC)", 
            "location": "Abu Dhabi, UAE", 
            "source": "Bayt UAE", 
            "link": "https://www.bayt.com"
        },
        {
            "title": "HR Specialist", 
            "company": "Al Futtaim Group", 
            "location": "Dubai, UAE", 
            "source": "Naukri Gulf", 
            "link": "https://www.naukrigulf.com"
        },
        {
            "title": "Software Engineer", 
            "company": "Emirates Airline", 
            "location": "Dubai, UAE", 
            "source": "GulfTalent", 
            "link": "https://www.gulftalent.com"
        },
        {
            "title": "Customer Service Executive",
            "company": "Majid Al Futtaim",
            "location": "Sharjah, UAE",
            "source": "Indeed UAE",
            "link": "https://uae.indeed.com"
        }
    ]
    
    # Put the sample jobs into our collector list
    collected_jobs.extend(sample_jobs)

    # Save all found jobs into our jobs.json pantry file
    with open("jobs.json", "w") as f:
        json.dump(collected_jobs, f, indent=4)
        
    print(f"Scraper finished! Successfully saved {len(collected_jobs)} jobs to jobs.json.")

if __name__ == "__main__":
    run_scraper()
