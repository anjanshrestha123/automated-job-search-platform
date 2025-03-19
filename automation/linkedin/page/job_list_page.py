from automation.linkedin.error_handler import handle_error
from automation.linkedin.page import questions_from_employer_page
from util.web_element_util import interact, fetch_elements_with_wait
from selenium.webdriver.common.by import By


def apply(browser_with_wait, browser):
    print('\n*** Page - Job List ***')
    current_page = 1

    while True:
        jobs = fetch_elements_with_wait(browser_with_wait, By.XPATH, '//*[@data-view-name="job-card"]')

        for job in jobs:
            is_job_applied = apply_job(browser_with_wait, job)

            if not is_job_applied:
                handle_error(browser)
                interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,
                         '[data-test-modal-close-btn]', 'X - Button')
                interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,
                         '[data-test-dialog-secondary-btn]', 'Discard - Button')

        current_page += 1
        if not interact(browser_with_wait, lambda button: button.click(), By.XPATH, "//button[contains(@class, 'jobs-search-pagination__indicator-button')][span[text()='{}']]".format(current_page), 'Next Page - Button'):
            break


def apply_job (browser_with_wait, job):
    job.click()
    if interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR, '[data-live-test-job-apply-button]', 'Easy Apply - Button'):
        while True:
            questions_from_employer_page.answer_questions(browser_with_wait)
            next_button_clicked = interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,'[data-live-test-easy-apply-next-button]', 'Next - Button')
            if next_button_clicked:
                errors = fetch_elements_with_wait(browser_with_wait, By.CSS_SELECTOR, '[data-test-form-element-error-messages]')

                if len(errors) > 0:
                    print('Job form is not properly filled')
                    return False
            else:
                break

        if interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,
                    '[data-live-test-easy-apply-review-button]', 'Review - Button') and \
                interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,
                         '[data-live-test-easy-apply-submit-button]', 'Submit application - Button'):
            print('Job Applied Successfully')
            interact(browser_with_wait, lambda button: button.click(), By.CSS_SELECTOR,
                     '[data-test-modal-close-btn]', 'X - Button')
            return True
    else:
        print('Job Already Applied')
        return True

    return False



