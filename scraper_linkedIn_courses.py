import requests
from bs4 import BeautifulSoup
url = 'https://www.linkedin.com/learning/search?trk=content-hub-home-page_guest_nav_menu_learning'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    course_listings = soup.find_all('li', {'class':'results-list__item'})
    for course in course_listings:
        title = course.find('h3', {'class': 'base-search-card__title'}).text.strip()
        created_by = course.find('h4', {'class': 'base-search-card__subtitle'}).text.strip()
        duration = course.find('div', {'class': 'search-entity-media__duration'}).text.strip()
        # Find the anchor tag containing the link
        anchor_tag = soup.find('a', class_='base-card__full-link')
        # Extract the 'href' attribute value
        if anchor_tag:
            href_link = anchor_tag['href']
        else:
            print("Anchor tag not found.")
        print(f"Title: {title}\Created By: {created_by}\nDuration: {duration}\nCourse Link: {href_link}\n")
else:
    print("Failed to fetch course listings.")


