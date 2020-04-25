from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    #задаем функцию для расчета
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    # считываем значение для переменной х, находим ткст для перемнной .text
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    # выполняем функцию расчета
    y = calc(x)
    # записываем ответ в поле
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    # прокручиваем страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")
    # или прокручиваем на центр кнопки button
    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    # ищем и кликаем в чекбокс
    check = browser.find_element_by_id('robotCheckbox')
    check.click()
    # ищем и кликаем в переключатель
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    # ищем и кликаем в кнопку
    sub = browser.find_element_by_css_selector('button')
    sub.click()

finally:

    time.sleep(10)
    browser.quit()