from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


#patc_chromedrie = executable_path="c:/chromedrive/chromedriver.exe"
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
    browser.get(link)

    x = browser.find_element_by_id("treasure").get_attribute("valuex")


    y = calc(x)
    # 4. Ввести ответ в текстовое поле.
    browser.find_element(By.ID, 'answer').send_keys(y)

    # 5. Отметить checkbox "I'm the robot".
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # 6. Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла