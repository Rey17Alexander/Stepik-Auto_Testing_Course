import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	time.sleep(3)
	number1 = browser.find_element_by_id("num1").text
	number2 = browser.find_element_by_id("num2").text
	summary = int(number1) + int(number2)


	select_list = Select(browser.find_element_by_id("dropdown"))
	select_list.select_by_value(str(summary))


	submit_button = browser.find_element_by_css_selector("button.btn.btn-default")
	submit_button.click()
finally:
	time.sleep(10)
	browser.quit()	

	print("\n\nNum1 =", number1)
	print("Num2 =", number2)
	print("Sum =", summary)
	print("Select_list =", select_list)
	print("Submit_button =", submit_button)