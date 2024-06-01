from util.web_element_util import interact
from util.web_element_util import get_text
from selenium.webdriver.common.by import By


def submit_application(browser_with_wait):
    if get_text(browser_with_wait, 5, By.XPATH, '//*[@id="ia-container"]/div/div/div/div/div[2]/div[2]/div/div/main/h1','Please review your application Title') == 'Please review your application':
        print('\n*** Page - Please review your application ***')
        return interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="ia-container"]/div/div/div/div/div[2]/div[2]/div/div/main/div[3]/div/button', 'Submit Your Application Button')
    else:
        print('\n*** Page Not Present - Please review your application ***')
        return False
