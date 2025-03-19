import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()