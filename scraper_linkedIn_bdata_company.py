import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

username='YOUR_BRIGHTDATA_USERNAME'
password='YOUR_BRIGHTDATA_PASSWORD'
auth=f'{username}:{password}'
host = 'YOUR_BRIGHTDATA_HOST'
browser_url = f'wss://{auth}@{host}'

async def main():
    async with async_playwright() as pw:
        print('connecting')
        browser = await pw.chromium.connect_over_cdp(browser_url)
        print('connected')
        page = await browser.new_page()
        print('goto')
        await page.goto('https://www.linkedin.com/company/spacex/', timeout=120000)
        print('done, evaluating')
        
        # Get the entire HTML content
        html_content = await page.evaluate('()=>document.documentElement.outerHTML')
        
        # Parse the HTML with Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the 'About us' description
        description_element = soup.select_one('.core-section-container[data-test-id="about-us"] p[data-test-id="about-us__description"]')
        description = description_element.text if description_element else None
        print('Description:')
        print(description)

        # Extract the 'Company size'
        company_size_element = soup.select_one('div[data-test-id="about-us__size"] dd')
        company_size = company_size_element.text.strip() if company_size_element else None
        print('Company size:')
        print(company_size)

        await browser.close()

# Run the async function
asyncio.run(main())
