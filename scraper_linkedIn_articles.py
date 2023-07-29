import requests
from bs4 import BeautifulSoup
url = 'https://www.linkedin.com/pulse/topics/home/?trk=guest_homepage-basic_guest_nav_menu_articles'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    article_listings = soup.find_all('div', {'class':'content-hub-entities'})
    for article in article_listings:
        title = article.find('h2', {'class': 'break-words'}).text.strip()
        description = article.find('p', {'class': 'content-description'}).text.strip()
        # Find the anchor tag containing the link
        anchor_tag = soup.find('a', class_='min-w-0')
        # Extract the 'href' attribute value
        if anchor_tag:
            href_link = anchor_tag['href']
        else:
            print("Anchor tag not found.")
        print(f"Title: {title}\nDescription: {description}\nArticle Link: {href_link}\n")
else:
    print("Failed to fetch article listings.")


