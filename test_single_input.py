import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_input_and_click(driver, index, text):
    inputs = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'input'))
    )
    inputs[index].send_keys(text)
    if index == 0:
        inputs[1].clear()
    else:
        inputs[0].clear()

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )
    button.click()

    result_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.result'))
    )
    return result_div

@pytest.mark.single_input_test
def test_fill_single_input(driver):
    url = 'https://all.zinkin.ru/bots/bot-work-selenium/i/38cb18ab-7433-449c-a7c8-f5fdcecda929/5/'
    driver.get(url)

    try:
        result_div = fill_input_and_click(driver, 0, 'Hello world!')
        assert result_div.text == 'Good'

        driver.get(url)
        result_div = fill_input_and_click(driver, 1, 'Hello world!')
        assert result_div.text == 'Good'
    except Exception as e:
        raise e