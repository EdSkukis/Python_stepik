from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:

    # 2. Заполнить текстовые поля: имя, фамилия, email.
    browser.find_element(By.NAME, 'firstname').send_keys('Эдуард')
    browser.find_element(By.NAME, 'lastname').send_keys('Скукис')
    browser.find_element(By.NAME, 'email').send_keys('edskikis@gmail.com')

    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
   # закрываем браузер после всех манипуляций
    browser.quit()
