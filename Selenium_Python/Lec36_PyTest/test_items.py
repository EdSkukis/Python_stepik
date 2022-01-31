# pytest --language=es test_items.py
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_support(browser):
    browser.get(link)
    #time.sleep(5)
    buttom = browser.find_element(By.CSS_SELECTOR,'button.btn')
    assert NoSuchElementException, "No create class button"

