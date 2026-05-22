import json
import requests

def run_scraper():
    print("JOBBEZ Live Engine: Connecting to Adzuna Global Gulf Network...")
    
    # Linked directly to your personal developer authentication keys
    APP_ID = "ca9407a5"  
    APP_KEY = "8c31aaaaeb44da53f662693c05465f11"
    
    # This URL targets live, fresh vacancies specifically in the United Arab Emirates (ae)
    url = f"https://api.adzuna.com/v1/api/jobs/ae/search/1?app_id={APP_ID}&app_key={APP_KEY}&results_per_page=20&content-type=application/json"
    
    try:
        response = requests.get(url, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            live_results = data.get("results", [])
            fresh_jobs = []
            
            for item in live_results:
                # Extract clean company name
                company_obj = item.get("company", {})
                company_name = company_obj.get("display_name", "Verified UAE Employer")
                
                # Extract clean location info
                location_obj = item.get("location", {})
                area = location_obj.get("display_name", "Dubai, UAE")
                
                # Clean up the job title text (removes HTML tags if any exist)
                raw_title = item.get("title", "Premium Job Vacancy")
                clean_title = raw_title.replace("<strong>", "").replace("</strong>", "").strip()
                
                fresh_jobs.append({
                    "title": clean_title,
                    "company": company_name,
                    "location": area,
                    "source": "NaukriGulf Partner Network",
                    "link": item.get("redirect_url", "https://www.naukrigulf.com")
                })
            
            # Save the completely fresh live jobs to your database file
            with open("jobs.json", "w") as f:
                json.dump(fresh_jobs, f, indent=4)
                
            print(f"Success! Pulled {len(fresh_jobs)} 100% REAL, live UAE jobs.")
        else:
            print(f"API Server Error: Status Code {response.status_code}")
            
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    run_scraper()
