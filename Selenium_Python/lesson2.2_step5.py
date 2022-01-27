from selenium import webdriver

try:
    browser = webdriver.Chrome(executable_path="c:/chromedrive/chromedriver.exe")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
   # закрываем браузер после всех манипуляций
    browser.quit()
