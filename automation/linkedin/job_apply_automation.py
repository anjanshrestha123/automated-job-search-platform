import traceback

import undetected_chromedriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from automation.linkedin.error_handler import handle_error
from automation.linkedin.page import login_page, job_list_page
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.os_manager import ChromeType




def apply_job():

    # Configure browser
    browser = configure_browser()

    try:
        job_search_url = 'https://www.linkedin.com/jobs/search/?currentJobId=4147957338&distance=25&f_AL=true&f_JT=F&f_SB2=6&f_WT=2&geoId=103644278&keywords=java%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD'

        print('\n*** Browsing [{}] ***'.format(job_search_url))
        browser.get(job_search_url)
        browser_with_wait = WebDriverWait(browser, 5)

        login_page.login(browser_with_wait, browser)
        job_list_page.apply(browser_with_wait, browser)

    except Exception as e:
        print("An unexpected error occurred during automation")
        traceback.print_exc()
        handle_error(browser)

    finally:
        # Close the browser session
        browser.quit()


def configure_browser():
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--user-data-dir=./resources/chromeprofile')
    chrome_options.add_argument('--profile-directory=Profile 1')

    # Configure browser
    service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    return webdriver.Chrome(service=service, options=chrome_options)
