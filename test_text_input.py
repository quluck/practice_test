import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_input_and_click(driver, text):
    text_input = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, 'input'))
    )
    text_input.send_keys(text)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )
    button.click()

    result_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.result'))
    )
    return result_div

@pytest.mark.text_input_test
def test_fill_text_input(driver):
    url = 'https://all.zinkin.ru/bots/bot-work-selenium/i/38cb18ab-7433-449c-a7c8-f5fdcecda929/4/'
    driver.get(url)

    try:
        result_div = fill_input_and_click(driver, 'Hello world!')
        assert result_div.text == 'Good'
    except Exception as e:
        raise e