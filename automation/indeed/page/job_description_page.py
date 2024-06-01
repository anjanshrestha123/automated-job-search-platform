from util.web_element_util import interact
from selenium.webdriver.common.by import By


def click_apply_button(browser_with_wait):
    print('\n*** Page - Job Description ***')
    return interact(browser_with_wait, lambda button: button.click(), By.ID, 'indeedApplyButton', 'Apply Now Button 1') or \
           interact(browser_with_wait, lambda button: button.click(), By.XPATH, '/html/body/div/div[2]/div[3]/div/div/div[1]/div[2]/div[5]/div[3]/div/div/div/button', 'Apply Now Button 2') or \
           interact(browser_with_wait, lambda button: button.click(), By.XPATH, '/html/body/div/div[2]/div[3]/div/div/div[1]/div[3]/div[6]/div[3]/div/div/div/button', 'Apply Now Button 3') or \
           interact(browser_with_wait, lambda button: button.click(), By.XPATH, '/html/body/div/div[2]/div[3]/div/div/div[1]/div[2]/div[6]/div[3]/div/div/div/button', 'Apply Now Button 4')
