import time
import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)


	x = int(browser.find_element_by_id("input_value").text)
	

	y = calc(x)


	main_input = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", main_input)
	main_input.send_keys(y)
	assert True


	robo_gender = browser.find_element_by_id("robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robo_gender)
	robo_gender.click()
	

	ruler = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", ruler)
	ruler.click()


	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()


finally:
	time.sleep(6)
	browser.quit()