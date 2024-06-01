import undetected_chromedriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse
from dto.job_status import JobStatus
from automation.indeed.page import job_description_page
from automation.indeed.page import login_page
from automation.indeed.page import add_resume_page
from automation.indeed.page import questions_from_employer_page
from automation.indeed.page import review_application_page
from config import config
import os



def apply_job(job_id):

    job_status = JobStatus.NOT_APPLIED

    # Configure browser
    browser = configure_browser()

    try:
        # Set up job info url
        params = {
            'jk': job_id
        }
        job_info_url = config.get_indeed_base_url() + '/viewjob/?' + urllib.parse.urlencode(params)

        print('\n*** Browsing [{}] ***'.format(job_info_url))
        browser.get(job_info_url)
        browser_with_wait = WebDriverWait(browser, 5)

        if job_description_page.click_apply_button(browser_with_wait) and \
                login_page.login(browser_with_wait, browser) and \
                add_resume_page.add_resume(browser_with_wait) and \
                questions_from_employer_page.answer_questions(browser_with_wait) and \
                review_application_page.submit_application(browser_with_wait):
            print('Job Applied Successfully')
            job_status = JobStatus.APPLIED
        else:
            print('Error during job automation for job id: [{}]'.format(job_id))
            job_status = handle_error(browser, job_id)

    except Exception as e:
        print("An unexpected error occurred during automation for job id: [{}] \n".format(job_id), e)
        job_status = handle_error(browser, job_id)

    finally:
        # Wait for the last browser execution
        time.sleep(3)

        # Refresh the browser to see if there is any alert
        browser.refresh()

        # Sleep for letting browser refresh and displaying alert
        time.sleep(2)

        # Handle the "cancel and leave" alert if present
        try:
            # For handling reload alert
            browser.switch_to.alert.accept()

            # For handling leave alert
            browser.switch_to.alert.accept()
        except:
            pass

        # Close the browser session
        browser.quit()

    return job_status


def configure_browser():
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--user-data-dir=./resources/chromeprofile')
    chrome_options.add_argument('--profile-directory=Profile 1')

    # Configure browser
    return webdriver.Chrome(options=chrome_options)


def handle_error(browser, job_id):
    # Create directory if it doesn't exist
    directory = './resources/error'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the screenshot path
    screenshot_path = os.path.join(directory, '{}_error.png'.format(job_id))

    # Check if the file exists and remove it if it does
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Save screenshot
    browser.save_screenshot(screenshot_path)

    return JobStatus.AUTOMATION_NOT_SUPPORTED
