from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element_by_class_name("btn")
    button.click()
    # соглашаемся  всплывающим окном
    alert = browser.switch_to.alert
    alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # считываем значение для переменной х, находим ткст для перемнной .text
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    # выполняем функцию расчета
    y = calc(x)

    answer = browser.find_element_by_css_selector("[name='text']")
    answer.send_keys(y)

    finish = browser.find_element_by_css_selector("button")
    finish.click()

finally:
    time.sleep(4)
    browser.quit()