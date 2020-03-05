import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element_by_id("book")
    book_button.click()
    assert True



    x = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "input_value"))).text
    y = calc(x)

    main_input = browser.find_element_by_class_name("form-control")
    main_input.send_keys(y)

    submit_button = browser.find_element_by_css_selector("[type = 'submit']")
    submit_button.click()




finally:
    time.sleep(6)
    browser.quit()