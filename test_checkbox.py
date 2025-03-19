import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.checkbox_test
def test_click_checkboxes(driver):
    url = 'https://all.zinkin.ru/bots/bot-work-selenium/i/38cb18ab-7433-449c-a7c8-f5fdcecda929/2/'
    driver.get(url)

    try:
        checkboxes = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="checkbox"]'))
        )
        
        if len(checkboxes) >= 3:
            for checkbox in checkboxes:
                checkbox.click()
            
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.TAG_NAME, 'button'))
            )
            button.click()

            result_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.result'))
            )
            assert result_div.text == 'Good'
        else:
            assert False, "Не найдено трех чекбоксов"
    except Exception as e:
        raise e