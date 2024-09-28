from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
driver.get("https://www.speedtest.net/")

try:
    # Wait for the "Go" button to be clickable and then click it
    go_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test"))
    )
    go_button.click()
    print("Clicked the 'Go' button to start the speed test.")

    # Introduce a delay to ensure the test has enough time to run (adjust if needed)
    time.sleep(60)  # Wait for 60 seconds (you can adjust the time as needed)

    # Wait for the download speed element to appear
    download_speed_element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "download-speed"))
    )
    upload_speed_element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "upload-speed"))
    )

    # Get the text (speed values) from the elements
    download_value = download_speed_element.text
    upload_value = upload_speed_element.text

    print(f"Download Speed: {download_value} Mbps")
    print(f"Upload Speed: {upload_value} Mbps")

except TimeoutException:
    print("Loading took too much time or the element was not found.")
except NoSuchElementException:
    print("Element not found on the page.")
finally:
    driver.quit()  # Close the browser window after the test

