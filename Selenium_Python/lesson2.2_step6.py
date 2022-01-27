from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element_by_id("input_value").text

    y = calc(x)
    # 4. Ввести ответ в текстовое поле.
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    # 5. Отметить checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # 6. Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()


    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
   # закрываем браузер после всех манипуляций
    browser.quit()
