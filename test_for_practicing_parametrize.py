import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

@pytest.mark.xfail
@pytest.mark.parametrize('lesson_num',
	["236898",
	"236899",
	"236905"])
def test_searching_ino_pieces_of_an_answer(browser, lesson_num):
	link = f"https://stepik.org/lesson/{lesson_num}/step/1"
	browser.get(link)
	assert True, "Browser hasn't started"

	text_area = browser.find_element_by_css_selector("textarea.textarea.string-quiz__textarea.ember-text-area.ember-view")
	assert True, "Text-area hasn't discovered"
	time_answer = math.log(int(time.time()))
	text_area.send_keys(str(time_answer))

	submit_button = browser.find_element_by_css_selector("button.submit-submission")
	submit_button.click()
	assert True, "The button hasn't clicked"

	optional_feedback = WDW(browser, 5).until(
		EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
	time.sleep(3)
	assert optional_feedback.text == "Correct!", "In this XFail test there is a piece of an answer"