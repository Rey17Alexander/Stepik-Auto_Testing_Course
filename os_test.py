import os
import time
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"


with open("empty_doc.txt", 'w') as file_to_upload:
	file_to_upload.write("This document is using to show that I can upload a file to the web page with Selenium toolkit")


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty_doc.txt')


try:
	browser = webdriver.Chrome()
	browser.get(link)
	time.sleep(1)


	first_name_input = browser.find_element_by_name("firstname")
	first_name_input.send_keys("Oleg")


	last_name_input = browser.find_element_by_name("lastname")
	last_name_input.send_keys("Nechiporenko")


	email_input = browser.find_element_by_name("email")
	email_input.send_keys("Oleg@olag.com")


	file_button = browser.find_element_by_id("file")
	file_button.send_keys(file_path)


	submit_button = browser.find_element_by_css_selector("button.btn.btn-primary")
	submit_button.click()
finally:
	time.sleep(6)
	browser.quit()