import asyncio
from playwright.async_api import async_playwright

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

        # Wait for the 'About us' section to be visible before extracting content
        await page.wait_for_selector('.core-section-container[data-test-id="about-us"]')

        # Extract the 'About us' description
        description_element = await page.query_selector('.core-section-container[data-test-id="about-us"] p[data-test-id="about-us__description"]')
        description = await description_element.inner_text()
        print('Description:')
        print(description)

        # Extract the 'Company size' (with error handling)
        company_size_element = await page.query_selector('div[data-test-id="about-us__size"] dd')
        company_size = await company_size_element.inner_text() if company_size_element else None
        if company_size:
            print('Company size:')
            print(company_size)

        await browser.close()

# Run the async function
asyncio.run(main())
