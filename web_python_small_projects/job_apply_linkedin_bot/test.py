import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Dictionary with prefilled data
prefilled_data = {
    'python_experience': '5',  # Example: 5 years of experience
    'autosar_experience': '3', # Example: 3 years of experience
    'github_experience': '4',  # Example: 4 years of experience
    'full_stack_experience': 'Yes' # Example: Yes or No
}

# Setup WebDriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if you don't need a GUI
# service = Service('path/to/chromedriver')  # Update with the path to your WebDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
# chrome_option.add_argument("--force-device-scale-factor=0.7")

driver =  webdriver.Chrome(options=chrome_option)

# Load the local HTML file
file_path = os.path.join(os.path.dirname(__file__), 'index.html')
driver.get(f'file:///{file_path}')

# Fill the text input fields
driver.find_element(By.ID, 'single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989438002-4540285602-numeric').send_keys(prefilled_data['python_experience'])
driver.find_element(By.ID, 'single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989438002-4540285594-numeric').send_keys(prefilled_data['autosar_experience'])
driver.find_element(By.ID, 'single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989438002-4540285586-numeric').send_keys(prefilled_data['github_experience'])

# Select from dropdown
dropdown = driver.find_element(By.ID, 'text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3989438002-4540285578-multipleChoice')
for option in dropdown.find_elements(By.TAG_NAME, 'option'):
    if option.text == prefilled_data['full_stack_experience']:
        option.click()
        break

# Optionally submit the form if there's a submit button
# submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')  # Update the selector if needed
# submit_button.click()

# Close the browser
time.sleep(1000)
driver.quit()
