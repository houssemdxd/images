import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the login page
driver.get('https://www.facebook.com')

# Print the title of the page
print("Page Title: ", driver.title)

# Wait for the "Decline optional cookies" button to be visible and click it
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Decline optional cookies")]'))
)
decline_button = driver.find_element(By.XPATH, '//button[contains(text(), "Decline optional cookies")]')
decline_button.click()
print("Clicked the 'Decline optional cookies' button")

# Generate the output.html file with the page source
html_file_path = './output.html'
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
print(f"Page source saved as {html_file_path}")


# Take a screenshot before clicking the login button
screenshot_folder = './folder1'
os.makedirs(screenshot_folder, exist_ok=True)  # Create the folder if it doesn't exist

timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_filename = f"{screenshot_folder}/screenshot_before_login_{timestamp}.png"
driver.save_screenshot(screenshot_filename)
print(f"Screenshot saved as {screenshot_filename}")


/*WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Email or phone number"]'))
)




# Wait for the email and password fields to be visible (increase wait time)
try:
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'email'))  # or use XPath here if ID is changing
    )
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'pass'))
    )
except Exception as e:
    print(f"Error while waiting for elements: {e}")
    print(driver.page_source)  # Print the page source for debugging

# Take a screenshot before clicking the login button
screenshot_folder = './folder1'
os.makedirs(screenshot_folder, exist_ok=True)  # Create the folder if it doesn't exist

timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_filename = f"{screenshot_folder}/screenshot_before_login_{timestamp}.png"
driver.save_screenshot(screenshot_filename)
print(f"Screenshot saved as {screenshot_filename}")




# Type the email and password into the respective fields
email_field = driver.find_element(By.ID, 'email')
password_field = driver.find_element(By.ID, 'pass')

email = 'your-email@example.com'  # Replace with your email
password = 'your-password'  # Replace with your password

email_field.send_keys(email)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.ID, 'loginbutton')
login_button.click()
print("Clicked the 'Log In' button")

# Wait for the page to load after login
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'userNavigationLabel'))  # Adjust if needed
)
*/
# Close the browser
driver.quit()

