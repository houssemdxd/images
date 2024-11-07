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

    # Take a screenshot after confirming email field is present
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_filename = f"emailimage_{timestamp}.png"
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

except Exception as e:
    print("Email field not found:", e)

# Close the browser
driver.quit()