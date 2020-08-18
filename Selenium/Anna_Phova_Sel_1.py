#1. Create automation framework for our test website
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 2. Go to : https://qasvus.wordpress.com
# 3. Use Chrome browser
# 4. Maximize browser window

print("Setting up page size")
driver = webdriver.Chrome()
driver.get('chrome://settings/')
time.sleep(2.5) # wait 2.5 seconds
print("Opening browser and navigating to testing link")
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
driver.get("https://qasvus.wordpress.com")
time.sleep(1.5)

driver.maximize_window()
time.sleep(1.5)
# 5. Print link(href) for header message "California Real Estate"
# 6. Print link(src) for first home image under "About us"

print("Printing link for California relal estate link and home image in About us section")
print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[contains(text(),'California Real Estate')]").get_attribute("href"))
time.sleep(1.5)
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
time.sleep(1.5)

# 7. Verify (do assert) "California Real Estate" in  website title
# 8. Print website title
print("Verifying that text California Real Estate")

assert "California Real Estate" in driver.title
print(driver.title)

#9.Find "Send Us a Message" and verify it's present on the web page

print('Verify that "Send Us a Message" on webpage')
driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
assert "Send Us a Message" in driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text

#10 Fill out and send the message form using the following tags:
# - XPath
# - ID
# - Name
# - Class_Name
# - Link_Text or Link_Partial_Text
print("Filling up Send message form")
driver.implicitly_wait(5)
driver.find_element(By.ID, "g2-name").send_keys("Hanna Puhoffa")
driver.find_element(By.NAME, "g2-email").send_keys("mytegnica@gmail.com")
driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("This is my testing message. I am sending this message to site to make sure that my script working fine :)")
time.sleep(2.5)
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").location_once_scrolled_into_view
driver.implicitly_wait(10)
time.sleep(2.5)
print("Submiting message")
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
time.sleep(2.5)

# 11. When the message will be send:
# - Find "go back" button (link) and using one of the tags above click it to go back to the Main page.

print("Navigating back to main page")
driver.find_element(By.LINK_TEXT, "go back").location_once_scrolled_into_view
print(driver.find_element(By.LINK_TEXT, "go back").get_attribute("href"))
time.sleep(1.5)
print('Finded go back button')
driver.find_element(By.LINK_TEXT, "go back").send_keys('\n')

#
# # 12. Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
print("Cheking if back to main page by find Submit button")
driver.find_element(By.CLASS_NAME, "pushbutton-wide")
print("type",(driver.find_element(By.CLASS_NAME, "pushbutton-wide")).get_attribute("type"))


# # # closing browser tab
driver.close()

