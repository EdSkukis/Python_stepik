from selenium import webdriver
import time


browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

try:
    browser.find_element_by_id("button")

finally:
    browser.quit()
