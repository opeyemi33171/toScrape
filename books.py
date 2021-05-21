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
driver.get(os.environ['BOOK_PAGE_URL'])

def get_links(driver):
    catergory_list = driver.find_element_by_class_name("nav-list")
    categories = catergory_list.find_elements_by_css_selector('li > ul > li > a')

    return categories

def get_books(markup):
    soup = get_bsoup(markup)
    product_pod = soup.find_all('article', class_='product_pod')

    return [item for item in product_pod]

def get_bsoup(markup):
    return BeautifulSoup(markup, 'html.parser')

bookCategoryLinks = get_links(driver)
lengthOfCategories = len(bookCategoryLinks)

for i in range(lengthOfCategories):
    category = get_links(driver)
    try:
        isOK = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'nav-list')))

        if isOK:
            category[i].click()

    except:
        pass


driver.quit()
