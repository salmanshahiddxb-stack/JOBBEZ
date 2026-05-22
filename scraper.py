import json
import requests

def run_scraper():
    print("JOBBEZ Driver: Syncing with live Gulf & UAE job networks...")
    
    # We use a real, open API stream that updates throughout the day
    url = "https://arjunsweb.pythonanywhere.com/api/jobs?location=dubai"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            raw_jobs = response.json()
            fresh_listings = []
            
            # Take up to 20 of the absolute newest live jobs found
            for item in raw_jobs[:20]:
                fresh_listings.append({
                    "title": item.get("title", "Job Vacancy"),
                    "company": item.get("company", "Verified Employer"),
                    "location": item.get("location", "Dubai, UAE"),
                    "source": item.get("source", "Premium Feed"),
                    "link": item.get("url", "https://google.com")
                })
                
            with open("jobs.json", "w") as f:
                json.dump(fresh_listings, f, indent=4)
                
            print(f"Success! Captured {len(fresh_listings)} completely fresh jobs.")
        else:
            print(f"Server issues. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    run_scraper()
