import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"


try:
	browser = webdriver.Chrome()
	browser.get(link)
	time.sleep(1)
	first_window_name = browser.window_handles[0]


	first_button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
	first_button.click()


	new_window_name = browser.window_handles[1]
	browser.switch_to.window(new_window_name)
	time.sleep(1)


	x = browser.find_element_by_id("input_value").text
	y = calc(x)


	answer_input = browser.find_element_by_id("answer")
	answer_input.send_keys(y)


	submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
	submit_button.click()
finally:
	time.sleep(6)
	browser.quit()