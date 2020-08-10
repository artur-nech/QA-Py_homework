#Import selenuim settings
import select
from telnetlib import EC

import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#setting up browser driver
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

#filling up form fields

print("Filling up form")
driver.implicitly_wait(5)
print("Fill up name and last name")
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Anna")
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[2]").send_keys("Test")
time.sleep(3)
print("Fill up email")
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/input[1]").send_keys("test@test.com")
time.sleep(3)
print("Fill up phone number")
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]").send_keys("555-555-55-55")
time.sleep(3)
print("Select product")
driver.find_element(By.ID, "radio-0000000e4" ).click()
time.sleep(3)
print("Fill up Quantity")
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/input[1]").send_keys("5")
time.sleep(3)
print("Select date")
driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//html//body//div//div//div//div//div[contains(text(),'10')]").click()
time.sleep(2)
print("Fill up address")
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[1]/input[1]").send_keys("2222 Sun st, apr 1")
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[3]/input[1]").send_keys("Testcity")
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[3]/input[2]").send_keys("CA")
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[2]/div[7]/div[1]/div[4]/input[1]").send_keys("11111")
time.sleep(3)
print("Select from Coutry dropdown")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Zambia')]").click()

print("Select from Dropdown dropdown")

driver.find_element(By.CSS_SELECTOR, "div:nth-child(8) div:nth-child(1) div:nth-child(3) div:nth-child(1) > select:nth-child(1)").click()
time.sleep(4)
driver.find_element_by_xpath("//*[contains(text(), 'Choice2')]").click()
time.sleep(4)

print("Select checkbox Multiple choice")
driver.find_element(By.ID,"checkbox-00000018-3").click()
time.sleep(2)
driver.find_element(By.XPATH,"//body/form[@id='form']/div/div/div[9]/div[1]/div[4]/div[1]/input[1]").send_keys("testing 1")

# print("Verification")
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']"))))
time.sleep(4)
print("Submitting form")
driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/button[1]").click()
time.sleep(3)

# closing browser tab
driver.close()

