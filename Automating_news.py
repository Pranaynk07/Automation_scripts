from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from datetime import datetime
import os
import sys
import traceback

try:
    # Detect if running as a compiled EXE
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    now = datetime.now()
    current_date = now.strftime("%d%m%Y")  # DDMMYYYY

    # ChromeDriver path
    if getattr(sys, 'frozen', False):
        # Expect chromedriver.exe in same folder as your .exe
        driver_path = os.path.join(application_path, "chromedriver.exe")
    else:
        driver_path = r"C:\Users\prana\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    website = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"

    # headless mode
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print("Launching ChromeDriver...")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website)

    print("Website loaded, collecting news...")

    # Scrolling to load more news
    for i in range(4):
        scroll_height = driver.execute_script("return window.innerHeight")
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        time.sleep(3)

    containers = driver.find_elements(
        by="xpath", value='//div[@class="IL9Cne"]')

    publishers = []
    headlines = []
    links = []

    for container in containers:
        publisher = container.find_element(by="xpath", value='./div').text
        headline = container.find_element(by="xpath", value='./a').text
        link = container.find_element(
            by="xpath", value='./a').get_attribute("href")

        publishers.append(publisher)
        headlines.append(headline)
        links.append(link)

    my_dict = {'Publisher': publishers,
               'Headline': headlines, 'News_Link': links}
    df_headlines = pd.DataFrame(my_dict)
    file_name = f'Headlines-{current_date}.csv'
    final_path = os.path.join(application_path, file_name)
    df_headlines.to_csv(final_path, index=False)

    print("News scraping complete!")
    print("Saved CSV at:", final_path)

except Exception as e:
    print("An error occurred:", e)
    print(traceback.format_exc())

finally:
    if driver:
        driver.quit()
