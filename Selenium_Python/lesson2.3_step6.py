from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def print_answer():
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

    print_answer()
finally:
    time.sleep(10)
   # закрываем браузер после всех манипуляций
    browser.quit()
