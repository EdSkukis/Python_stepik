from selenium import webdriver
import time
import math



patc_chromedrie = executable_path="c:/chromedrive/chromedriver.exe"
link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
    browser.get(link)
    value = 'input'
    elements = browser.find_elements_by_tag_name(value)
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла