from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
counter = 0

def get_links(driver):
    driver.get(os.environ['BOOK_PAGE_URL'])

    catergory_list = driver.find_element_by_class_name("nav-list")
    categories = catergory_list.find_elements_by_css_selector('li > ul > li > a')

    return categories

cat_number = len(get_links(driver))

def get_books(markup):
    soup = BeautifulSoup(markup, 'html.parser')
    product_pod = soup.find_all('article', class_='product_pod')

    return [item for item in product_pod]


for i in range(cat_number):
    category = get_links(driver)
    try:
        wait_till_loaded(driver,'nav-list', 10)

        if isOK:
            click_link(category[i])
            books = get_books(urlopen(driver.current_url).read())

            i += 1

    except:
        i += 1
        pass

def wait_till_loaded(driver, element, time):
    isOK = WebDriverWait(driver, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, elements)))

def click_link(link):
    link.click()
driver.quit()
