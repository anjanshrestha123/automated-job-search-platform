import os
from datetime import datetime

def handle_error(browser):
    # Create directory if it doesn't exist
    directory = './resources/error/linkedin'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the screenshot path
    screenshot_path = os.path.join(directory, '{}_error.png'.format(datetime.now().strftime("%Y%m%d%H%M%S")))

    # Check if the file exists and remove it if it does
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Save screenshot
    browser.save_screenshot(screenshot_path)