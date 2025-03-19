import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_buttons(driver):
    buttons = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'button'))
    )
    if len(buttons) >= 2:
        buttons[0].click()
        buttons[1].click()
    else:
        raise AssertionError("Не найдено двух кнопок")

@pytest.mark.button_test
def test_click_buttons(driver):
    url = 'https://all.zinkin.ru/bots/bot-work-selenium/i/38cb18ab-7433-449c-a7c8-f5fdcecda929/1/'
    driver.get(url)

    try:
        click_buttons(driver)

        result_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.result'))
        )
        assert result_div.text == 'Good'
    except Exception as e:
        raise e