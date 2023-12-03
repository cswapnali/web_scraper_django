from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import time
from datetime import datetime, timedelta
import re

def scrape_news(query):
    all_details = []

    url = f"https://www.cnbc.com/search/?query={query}&qsearchterm={query}"

    chrome_options = Options()
    chrome_options.add_argument("--disable-popup-blocking")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    browser.get(url)
    browser.maximize_window()
    wait = WebDriverWait(browser, 120)

    for _ in range(2):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    details = browser.find_elements(By.XPATH, "//a[@class='resultlink']")
    
    i = 1
    all_links = []
    for d in details:
        try:
            link = d.get_attribute('href')
            all_links.append(link)
        except StaleElementReferenceException:
            continue
        if i >= 5:
            break
        i+=1

    print(len(all_links))
    all_links = list(set(all_links))
    print(len(all_links))

    for i, link in enumerate(all_links):
        name, summary, pub_date = scrape_headline_and_summary(browser, wait, link)

        end_date = datetime.today()
        start_date = end_date - timedelta(days=5)

        if name != 'NA' and summary != 'NA' and pub_date != 'NA':
            pattern = re.compile(r"Published (.* \d{4})")
            result = pattern.search(pub_date)

            if result is not None:
                published_date = datetime.strptime(result.group(0), 'Published %a, %b %d %Y')

                if start_date <= published_date <= end_date:
                    link_details = {'Name': name, 'Summary': summary, 'Pub_Date': pub_date}
                        
                    all_details.append(link_details)
                    print(i, name)

        time.sleep(2)
    browser.quit()

    return all_details

def scrape_headline_and_summary(browser, wait, link):
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(link)
    time.sleep(2)

    try:
        name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ArticleHeader-headerContentContainer']//h1")))
        name = name_element.text
    except:
        try:
            name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='ArticleHeader-styles-makeit-headline--l_iUX']")))
            name = name_element.text
        except:
            try:
                name_element = wait.until(EC.presence_of_all_element_located((By.XPATH, "//h1[@class='ClipPlayer-clipPlayerIntroTitle']")))
                name = name_element.text
            except:
                name = 'NA'

    try:
        summary_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='group']//p")))
        summary_data = [element.text for element in summary_elements]
        summary = ' '.join(summary_data)
    except:
        try:
            summary_elements = wait.until(EC.presence_of_all_element_located((By.XPATH, "//div[@class='ClipPlayer-clipPlayerIntroSummary']")))
            summary = summary_elements.text
        except:
            summary = 'NA'

    try:
        pub_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ArticleHeader-time']//time")))
        pub_date =  pub_element.text
    except:
        try:
            pub_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ArticleHeader-styles-makeit-time--hKeEh']//time")))
            pub_date =  pub_element.text
        except:
            try:
                pub_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ClipPlayer-clipPlayerIntroTime']")))
                pub_date =  pub_element.text
            except:
                pub_date = 'NA'

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    return name, summary, pub_date
