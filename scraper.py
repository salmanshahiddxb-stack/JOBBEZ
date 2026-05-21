import json
import requests

def run_scraper():
    print("JOBBEZ Driver: Heading out to collect real live jobs...")
    
    # This is an open API that collects real jobs across the web
    # We filter it to look for jobs in the UAE/Dubai
    url = "https://arjunsweb.pythonanywhere.com/api/jobs?location=dubai"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            raw_data = response.json()
            real_jobs = []
            
            # Translate the external data structure into our JOBBEZ structure
            for item in raw_data[:20]:  # Let's grab the top 20 freshest jobs
                job_card = {
                    "title": item.get("title", "Job Opening"),
                    "company": item.get("company", "Confidential Company"),
                    "location": item.get("location", "Dubai, UAE"),
                    "source": item.get("source", "Web Aggregator"),
                    "link": item.get("url", "https://www.google.com")
                }
                real_jobs.append(job_card)
                
            # Save the real live jobs to our pantry!
            with open("jobs.json", "w") as f:
                json.dump(real_jobs, f, indent=4)
                
            print(f"Success! Found and saved {len(real_jobs)} live jobs to jobs.json.")
            
        else:
            print(f"Server responded with error code: {response.status_code}")
            
    except Exception as e:
        print(f"Could not connect to live servers right now: {e}")

if __name__ == "__main__":
    run_scraper()
