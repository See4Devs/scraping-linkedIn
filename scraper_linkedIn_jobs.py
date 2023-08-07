import requests
from bs4 import BeautifulSoup
url = 'https://www.linkedin.com/jobs/search?keywords=Frontend%20Developer&location=United%20States&pageNum=0'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = soup.find_all('div', {'class':'job-search-card'})
    for job in job_listings:
        title = job.find('h3', {'class': 'base-search-card__title'}).text.strip()
        company = job.find('a', {'class': 'hidden-nested-link'}).text.strip()
        location = job.find('span', {'class': 'job-search-card__location'}).text.strip()
        anchor_tag = job.find('a', class_='base-card__full-link')
        href_link = anchor_tag['href']
        print(f"Title: {title}\nCompany: {company}\nLocation: {location}\nJob Link: {href_link}\n")
else:
    print("Failed to fetch job listings.")


