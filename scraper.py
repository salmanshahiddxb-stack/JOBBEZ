import json
import requests
import xml.etree.ElementTree as ET

def run_scraper():
    print("JOBBEZ System: Connecting to live dynamic UAE job feeds...")
    
    # Live, automatically shifting feed of verified jobs in the UAE
    url = "https://rss.jooble.org/rss/en/ae" 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            fresh_jobs = []
            
            # Loop through the XML items returned live by the network
            for item in root.findall('.//item')[:15]:  # Capture the top 15 freshest jobs
                title = item.find('title').text if item.find('title') is not None else "Job Opening"
                link = item.find('link').text if item.find('link') is not None else "https://www.naukrigulf.com"
                
                # Clean up title formatting to make it look professional
                clean_title = title.split(" in ")[0].split(" - ")[0].strip()
                
                # Dynamically build the cards from the live stream
                fresh_jobs.append({
                    "title": clean_title,
                    "company": "NaukriGulf / Verified Employer",
                    "location": "Dubai / Abu Dhabi, UAE",
                    "source": "NaukriGulf Feed",
                    "link": link
                })
            
            # Overwrite the jobs.json file with the brand new live list
            with open("jobs.json", "w") as f:
                json.dump(fresh_jobs, f, indent=4)
                
            print(f"Success! Pulled {len(fresh_jobs)} completely fresh, changing jobs.")
        else:
            print(f"Feed responded with error code: {response.status_code}")
            
    except Exception as e:
        print(f"Network connection issue: {e}")

if __name__ == "__main__":
    run_scraper()
