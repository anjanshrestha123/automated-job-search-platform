from util.web_element_util import interact
from selenium.webdriver.common.by import By
from util.web_element_util import send_keys_and_enter
from selenium.webdriver.support import expected_conditions as EC


def login(browser_with_wait, browser):
    print('\n*** Page - Login ***')
    if interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button', 'Sign In Button'):
        if interact(browser_with_wait, lambda input: send_keys_and_enter(input, '<>'), By.ID, 'base-sign-in-modal_session_key','Email or Phone Input') and \
                interact(browser_with_wait, lambda input: send_keys_and_enter(input, '<>'), By.ID, 'base-sign-in-modal_session_password', 'Password Input'):
            browser.switch_to.window(browser.window_handles[0])
            return True
        else:
            return False
    else:
        print('User Already Logged In')
        return True
