from util.web_element_util import interact
from selenium.webdriver.common.by import By
from util.web_element_util import send_keys_and_enter
from selenium.webdriver.support import expected_conditions as EC


def login(browser_with_wait, browser):
    print('\n*** Page - Login ***')
    if interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="googleContainer"]/button', 'Continue With Google Button'):
        # Wait for the new window or frame and switch to it
        browser_with_wait.until(EC.number_of_windows_to_be(2))
        browser.switch_to.window(browser.window_handles[1])

        if interact(browser_with_wait, lambda input: send_keys_and_enter(input, 'anjan.rme2@gmail.com'), By.ID, 'identifierId','Google Email Address Login Input') and \
                interact(browser_with_wait, lambda input: send_keys_and_enter(input, 'Gr@bidstha312'), By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input', 'Google Password Login Input'):
            browser.switch_to.window(browser.window_handles[0])
            return True
        else:
            return False
    else:
        print('User Already Logged In')
        return True
