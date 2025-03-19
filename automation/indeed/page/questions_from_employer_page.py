from util.web_element_util import interact
from util.web_element_util import get_text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import google.generativeai as genai
import re


def answer_questions(browser_with_wait):
    if get_text(browser_with_wait, 5,  By.XPATH, '//*[@id="ia-container"]/div/div[1]/div/div/div[2]/div[2]/div/div/main/h1', 'Answer these questions from the employer Title') == 'Answer these questions from the employer':
        print('\n*** Page - Answer these questions from the employer ***')

        # Read profile
        profile = open('./resources/input/profile.txt', 'r').read()

        # fill_text_elements
        fill_text_elements(browser_with_wait, profile, 'input')

        # fill_text area
        fill_text_elements(browser_with_wait, profile, 'textarea')

        # select_radio_button
        select_radio_buttons(browser_with_wait, profile)

        # Dropdown
        select_dropdown_options(browser_with_wait, profile)

        # Checkbox
        check_checkboxes(browser_with_wait, profile)

        return interact(browser_with_wait, lambda button: button.click(), By.XPATH, '//*[@id="ia-container"]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button', 'Continue Button')
    else:
        print('\n*** Page Not Present - Answer these questions from the employer ***')
        return True


# Function to check checkboxes
def check_checkboxes(browser_with_wait, profile):
    # Locate all checkbox elements
    checkbox_groups = browser_with_wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@role="group"]')))

    for group in checkbox_groups:
        # Extract the label text associated with the checkbox
        try:
            question_text = group.accessible_name
        except:
            question_text = "Question text not found"
        print("Question:", question_text)

        group_child_elements = group.find_elements(By.XPATH, ".//*")
        checkboxes = list( filter(lambda x: x.aria_role == 'checkbox', group_child_elements))

        for checkbox in checkboxes:
            try:
                response = genai.generate_text(
                         prompt="Strictly Answer in 0 or 1. Question = {} . My profile = {}".format(question_text + checkbox.accessible_name,
                                                                             profile)).result

                try:
                     desired_answer = 'YES' in response.upper().split(' ') or '1' in response.upper().split(' ')
                except:
                     print("Answer not found")
                     desired_answer = False

                # Check the checkbox if the label matches the desired text
                if desired_answer:
                    # interact(browser_with_wait, lambda button: button.click(), By.ID, 'input-q_fdf9529ba123a0b3a0368ca320a3af86-0',
                    #          'Pronouns - He/Him Selection Radio Selection')

                    checkbox.click()

            except Exception as e:
                print("No unselected checkbox found in this group: Error: {}".format(e))


def fill_text_elements(browser_with_wait, profile, type):
    elements = browser_with_wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, type)))

    for element in elements:
        element_type = element.get_attribute('type')
        if element_type in ['text', 'textarea', 'email', 'password', 'number', 'date', 'search', 'tel', 'url', None] \
                and len(element.accessible_name) > 0:  # None for textareas
            response = genai.generate_text(
                prompt="Find answer to: Question: {}. My profile = {} ".format(element.accessible_name,
                                                                    profile)).result

            if element_type == 'number':
                try:
                    element.send_keys(int(re.findall(r'\d+', response)[0]))
                except Exception as e:
                    print('Error occurred during sending number to the element with response {}, Error: {}'.format(response, e))
                    element.send_keys(0)
            else:
                element.send_keys(response)


def select_radio_buttons(browser_with_wait, profile):
    # TODO: make it dynamic
    radio_groups = browser_with_wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@role="radiogroup"]')))

    for group in radio_groups:
        # Extract the question text from the legend element
        try:
            question_text = group.accessible_name
        except:
            question_text = "Question text not found"

        print("Question:", question_text)

        group_child_elements = group.find_elements(By.XPATH, ".//*")
        options = list(map(lambda y: y.accessible_name, filter(lambda x: x.aria_role == 'radio', group_child_elements)))

        # for radio_button in radio_buttons:
        #     label_text = radio_button.find_element(By.XPATH, './following-sibling::span').text
        #     options.append(label_text)


        # Find the first unselected radio button within the group
        try:
            response = genai.generate_text(
                prompt="Give me the option with the exact text without any filler words. Question = {}, options={}, My profile = {} ".format(
                    question_text, options,
                    profile)).result

            answer = list(filter(lambda x: x.upper() in response.upper() or response.upper() in x.upper(), options))[0]

            print(answer)

            radio_button = group.find_element(By.XPATH, f'.//span[contains(text(), "{answer}")]/preceding-sibling::input[@type="radio"]')
            radio_button.click()
        except Exception as e:
            print("No unselected radio button found in this group: Error: {}".format(e))


def select_dropdown_options(browser_with_wait, profile):
    # Locate all dropdown elements
    dropdowns = browser_with_wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select')))

    for dropdown in dropdowns:
        try:
            question_text = dropdown.accessible_name
        except:
            question_text = "Question text not found"
        print("Question:", question_text)

        options = [option.text for option in Select(dropdown).options]

        # Find the first unselected radio button within the group
        try:
            response = genai.generate_text(
                prompt="Give me the option with the exact text without any filler words. Question = {}, options={}, My profile = {} ".format(
                    question_text, options,
                    profile)).result

            answer = list(filter(lambda x: x.upper() in response.upper(), options))[0]

            if options:
                Select(dropdown).select_by_visible_text(answer)
                print("Answer:", answer)
            else:
                print("No options found for this dropdown")

        except Exception as e:
            print("No dropdown found: Error: {}".format(e))