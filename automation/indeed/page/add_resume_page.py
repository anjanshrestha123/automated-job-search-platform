from util.web_element_util import interact
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def add_resume(browser_with_wait):
    print('\n*** Page - Add a resume for the employer ***')

    return interact(browser_with_wait, lambda button: button.click(), By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[2]/div/fieldset/div[3]', 'Original Resume Selection Button') and \
           click_continue_button(browser_with_wait)


def click_continue_button(browser_with_wait):
    buttons = browser_with_wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))

    for button in buttons:
        # Check if the button has the text "Continue"
        if button.text == "Continue":
            button.click()
            return True
    return False