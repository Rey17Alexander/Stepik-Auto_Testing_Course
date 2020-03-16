from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	time.sleep(3)
#2 условие
	treasure = browser.find_element_by_id("treasure")
#3 условие
	x = treasure.get_attribute("valuex")
#4 условие
	y = calc(x)
#5 условие
	main_input = browser.find_element_by_id("answer")
	main_input.send_keys(y)
#6 условие
	robo_gender = browser.find_element_by_id("robotCheckbox")
	robo_gender.click()
#7 условие
	ruler = browser.find_element_by_id("robotsRule")
	ruler.click()
#8 условие 
	submit_button = browser.find_element_by_css_selector("button.btn.btn-default")
	submit_button.click()
finally:
	time.sleep(15)
	browser.quit()

	print("\n\nX =", x_element, "\n\nType (x) =", type(x_element))