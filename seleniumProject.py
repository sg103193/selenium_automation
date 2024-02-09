#A selenium project to automate buying of book from bookchor website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.bookchor.com/")
driver.maximize_window()                    #to full screen the window

search = driver.find_element(By.TAG_NAME, "input")
search.clear()
search.send_keys("Till The Last Breath")        #to input in text field
btn = driver.find_element(By.XPATH, "//button[contains(@onclick, 'handleSearch')]")

btn.click()

book = driver.find_element(By.XPATH, "//a[contains(@href, 'till-the-last-breath')]")
book.click()

addToCartbtn = driver.find_element(By.XPATH, "//button[text()='Add to Cart']")
addToCartbtn.click()

time.sleep(5)
driver.quit()