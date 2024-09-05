import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        logger.info(f"Sending request to {url}")
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code != 200:
            logger.error(f"Failed to load page. Status: {response.status_code}")
            return f"Error: HTTP status {response.status_code}"
        
        logger.info("Page loaded successfully")
        return response.text

    except Exception as e:
        logger.error(f"Error scraping website: {str(e)}", exc_info=True)
        return f"Error scraping website: {str(e)}"

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return ""

def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()

    cleaned_content = soup.get_text()
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
   
    return cleaned_content

def split_dom_content(cleaned_content, max_length=15000):
    batches = [
        cleaned_content[i:i + max_length] for i in range(0, len(cleaned_content), max_length)
    ]
    return batches

#SBR_WEBDRIVER = 'https://brd-customer-hl_f8828f1a-zone-ai:t46p4oin5ktc@brd.superproxy.io:9515'

def  scrape_websites(website):
    pass
    """
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating...')
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')

        #CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])

        print('Navigated! Scraping page content...')
        html = driver.page_source
        print('Scraped! Closing connection...')
    
        return html    
    """

    """print("Scraping website")
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=Service(chrome_driver_path))

    try:
        driver.get(website)
        time.sleep(5)
        html = driver.page_source
        print("website scraped")
        time.sleep(5)

        return html
    
    finally:
        driver.quit()
"""
"""def extract_body_content(html):

    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    else:
        return ""

def clean_html(html):

    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()

    cleaned_content = soup.get_text()
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
   
    return cleaned_content

def split_dom_content(cleaned_content,max_length=6000):
    batches = [
        cleaned_content[i:i + max_length] for i in range(0, len(cleaned_content), max_length)
    ]
    return batches

"""