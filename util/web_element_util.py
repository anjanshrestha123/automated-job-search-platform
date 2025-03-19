from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def interact(browser_with_wait, web_element_action, by, web_element_text, web_element_description):
    try:
        time.sleep(1)
        # TODO: move mouse position
        web_element = browser_with_wait.until(EC.presence_of_element_located((by, web_element_text)))
        web_element_action(web_element)
        print('Interaction Successful With [{}]'.format(web_element_description))
        return True
    except Exception as e:
        print('[{}] is not present'.format(web_element_description))
        return False


def fetch_elements_with_wait(browser_with_wait, by, web_element_text):
    try:
        time.sleep(1)
        # TODO: move mouse position
        web_elements = browser_with_wait.until(EC.presence_of_all_elements_located((by, web_element_text)))
        return web_elements
    except Exception as e:
        print('[{}] is not present'.format(web_element_text))
        return []


def get_text(browser_with_wait, sleep_time, by, web_element_text, web_element_description):
    try:
        time.sleep(sleep_time)
        web_element = browser_with_wait.until(EC.presence_of_element_located((by, web_element_text)))
        return web_element.text
    except Exception as e:
        print('[{}] is not present'.format(web_element_description))
        return None


def send_keys_and_enter(input, text):
    input.send_keys(text)
    input.send_keys(Keys.RETURN)
