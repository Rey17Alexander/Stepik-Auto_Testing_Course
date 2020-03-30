import pytest
from selenium import webdriver

@pytest.fixture(scope = 'function')
def browser():
	print("\nBrowser runs...")
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	yield browser
	print("\nBrowser closed.")
	browser.quit()