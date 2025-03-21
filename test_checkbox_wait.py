import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_checkbox_and_button(driver):
    checkbox = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="checkbox"]'))
    )
    checkbox.click()

    WebDriverWait(driver, 3).until(lambda x: True)

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )
    button.click()

@pytest.mark.checkbox_wait_test
def test_checkbox_wait(driver):
    url = 'https://all.zinkin.ru/bots/bot-work-selenium/i/38cb18ab-7433-449c-a7c8-f5fdcecda929/6/'
    driver.get(url)

    try:
        click_checkbox_and_button(driver)

        result_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.result'))
        )
        assert result_div.text == 'Good'
    except Exception as e:
        raise e