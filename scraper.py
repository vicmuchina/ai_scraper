"""import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service"""
import time 
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

SBR_WEBDRIVER = 'https://brd-customer-hl_f8828f1a-zone-ai:t46p4oin5ktc@brd.superproxy.io:9515'

def  scrape_website(website):

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
    

    """  print("Scraping website")
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
            driver.quit()"""

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

def split_dom_content(cleaned_content,max_length=6000):
    batches = [
        cleaned_content[i:i + max_length] for i in range(0, len(cleaned_content), max_length)
    ]
    return batches

