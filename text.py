import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start an undetected ChromeDriver instance
driver = uc.Chrome()

# Go to a website
driver.get("https://example.com")

# Locate an element using XPath
element = driver.find_element(By.XPATH, '//*[@id="some-id"]')

# Perform actions (e.g., clicking, sending text)
element.click()

# Optional: send keys if needed
element.send_keys("Some Text" + Keys.RETURN)

# Close the driver when done
driver.quit()
