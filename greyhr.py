from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Credentials stored in environment variables for security
username = os.getenv('GREYTHR_USERNAME')
password = os.getenv('GREYTHR_PASSWORD')
url = "https://hgtl.greythr.com"

# Set up the Chrome driver in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Required for headless mode in some systems

try:
    # Initialize the WebDriver with headless options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, timeout=10)

    # Perform login and button clicking
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/uas-portal/div/div/main/div/section/div[1]/o-auth/section/div/app-login/section/div/div/div/form/button'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-container > .hydrated'))).click()

    time.sleep(60)  # Keep browser open for 1 minute to confirm the actions
    print("Attendance marked successfully!")

except Exception as ex:
    print(f"An error occurred: {ex}")

finally:
    driver.quit()
