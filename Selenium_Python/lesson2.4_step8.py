from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def print_answer():
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    # Нажать на кнопку "Book"
    browser.find_element(By.ID, 'book').click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.ID, 'solve').click()
    print_answer()
finally:
    browser.quit()
