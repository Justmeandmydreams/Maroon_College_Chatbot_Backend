import requests
from bs4 import BeautifulSoup
import json

# College website to scrape
URLS = [
    "https://krct.ac.in/",
    "https://krct.ac.in/departments/",
    "https://krct.ac.in/admission/",
    "https://krct.ac.in/placement/"
]

college_data = []

for url in URLS:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script and style tags
        for tag in soup(["script", "style"]):
            tag.extract()

        text = soup.get_text(separator=" ", strip=True)

        college_data.append({
            "url": url,
            "content": text[:10000]
        })

    except Exception as e:
        print(f"Error scraping {url}: {e}")

with open("college_data.json", "w", encoding="utf-8") as file:
    json.dump(college_data, file, indent=4)

print("College website data saved to college_data.json")