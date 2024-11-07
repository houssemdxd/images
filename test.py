import time
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

# Open Facebook's login page
driver.get('https://www.facebook.com')

# Print the title of the page
print("Page Title: ", driver.title)

# Wait for the page to load completely
driver.implicitly_wait(5)

# Wait for the "Decline optional cookies" button to be clickable and click it
try:
    decline_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Decline optional cookies']"))
    )
    decline_button.click()
    print("Clicked the 'Decline optional cookies' button")
except Exception as e:
    print(f"Error: {e}")

# Wait for the email field to be visible
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    print("Email exists")

    # Type "aaaa" into the email field
    email_field.send_keys("khalfaouihoussemeddine94@gmail.com")
    print('Typed "aaaa" into the email field')

except Exception as e:
    print("Email field not found:", e)

# Wait for the password field to be visible
try:
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'pass'))
    )
    print("Password field exists")

    # Type "password123" into the password field
    password_field.send_keys("password123")
    print('Typed "password123" into the password field')

except Exception as e:
    print("Password field not found:", e)

# Wait for the login button to be visible and clickable
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'login'))
    )
    print("Login button found")

    # Click the login button
    login_button.click()
    print("Clicked the login button")
    driver.implicitly_wait(5)

    # Take a screenshot after clicking the login button
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_filename = f"login_button_clicked_{timestamp}.png"
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

except Exception as e:
    print("Login button not found:", e)

# Close the browser
driver.quit()
