from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = 916#browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
   # закрываем браузер после всех манипуляций
    browser.quit()
