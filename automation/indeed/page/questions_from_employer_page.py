from util.web_element_util import interact
from util.web_element_util import get_text
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta


def answer_questions(browser_with_wait):
    if get_text(browser_with_wait, 5,  By.XPATH, '//*[@id="ia-container"]/div/div[1]/div/div/div[2]/div[2]/div/div/main/h1', 'Answer these questions from the employer Title') == 'Answer these questions from the employer':
        print('\n*** Page - Answer these questions from the employer ***')
        interact(browser_with_wait, lambda input: input.send_keys('4694649263'), By.ID,'input-q_6025df0e32277dafea5ee3a0678080e0', 'Phone Number Input')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_fdf9529ba123a0b3a0368ca320a3af86-0','Pronouns - He/Him Selection Radio Selection')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_daa4d9997b1076a12efb15e0a1b5f6f5-0','Proof of Authorization - Yes Radio Selection')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_19ce353618af9409a14cacecfea8011e-1','Require employer sponsorship 1 - No Radio Selection')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_260adc7ee996212867cb6545fcd987da-1','Require employer sponsorship 2 - No Radio Selection')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_9255d01a8265947d10a99ba12a591567-0','Can you work legally in US? - Yes Radio Selection')
        interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_7523d29b4ebaa63a44e0c62a8151eeed-1', 'Contact about future opportunities - No Radio Selection')

        start_date = (datetime.now() + timedelta(days=30)).strftime('%m/%d/%Y')
        interact(browser_with_wait, lambda element: element.send_keys(start_date), By.ID, 'input-q_192bc87eed20e9e594cbf3156f90e19c', 'What is the earliest date you could start?')

        return interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="ia-container"]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button', 'Continue Button')
    else:
        print('\n*** Page Not Present - Answer these questions from the employer ***')
        return True