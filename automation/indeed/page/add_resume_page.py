from util.web_element_util import interact
from selenium.webdriver.common.by import By


def add_resume(browser_with_wait):
    print('\n*** Page - Add a resume for the employer ***')
    return interact(browser_with_wait, lambda button: button.click(), By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]', 'Original Resume Selection Button') and \
           interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="ia-container"]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button', 'Continue Button')

