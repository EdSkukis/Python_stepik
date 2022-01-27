from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# тест для первой ссылки
try:
    link1 = "http://suninjuly.github.io/registration2.html"

    driver = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
    driver.get(link1)

    driver.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys("Albert")
    driver.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys("Einstein")
    driver.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys("albert@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    driver.quit()

# тест для второй ссылки
try:
    link2 = "http://suninjuly.github.io/registration2.html"

    driver = webdriver.Chrome()
    driver.get(link2)

    driver.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input").send_keys("Albert")
    driver.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input").send_keys("Einstein")
    driver.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input").send_keys("albert@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(10)
    driver.quit()


