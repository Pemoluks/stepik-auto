from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    # берем значение атрибута (.get_attribute) и записываем в х
    sund = browser.find_element_by_id("treasure")
    x = sund.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    sub = browser.find_element_by_css_selector('button')
    sub.click()

finally:

    time.sleep(10)
    browser.quit()

# str