from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os

selenium_host = os.environ.get("SELENIUM_HOST")
password = os.environ.get("PASSWORD")
router = os.environ.get("ROUTER_IP")

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor=f"http://{selenium_host}:4444/wd/hub",
    options=options
)

wait = WebDriverWait(driver,10)

driver.get(f"http://admin:{password}@{router}/index.cgi/reboot_main")
driver.find_element(By.XPATH, '//*[@id="UPDATE_BUTTON"]').click()
wait.until(expected_conditions.alert_is_present())
driver.switch_to.alert.accept()
driver.quit()
