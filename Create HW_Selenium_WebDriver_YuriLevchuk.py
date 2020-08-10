"""
SeleniumWebdriver tasks:
1. Create automation framework for our test website
2. Go to : https://qasvus.wordpress.com
3. Use Chrome browser
4. Maximize browser window
5. Print link(href) for header message "California Real Estate"
6. Print link(src) for first home image under "About us"
7. Verify (do assert) "California Real Estate" in  website title
8. Print website title
9. Find "Send Us a Message" and verify it's present on the web page
10. Fill out and send the message form using the following tags:
- XPath
- ID
- Name
- Class_Name
- Link_Text or Link_Partial_Text
11. When the message will be send:
- Find "go back" button (link) and using one of the tags above click it to go back to the Main page.
12. Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
"""

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # import time for setting exact browser pause,

# e.g., via time.sleep(0.5) vs. driver.implicitly_wait(0.5)

driver = webdriver.Chrome()  # use Chrome browser
driver.get("https://qasvus.wordpress.com/")  # go to : https://qasvus.wordpress.com
time.sleep(1.5)  # wait 1.5 seconds
driver.maximize_window()  # maximize browser window
time.sleep(2.5)  # wait 2.5 seconds

driver.get('chrome://settings/')
time.sleep(2.5)  # wait 2.5 seconds
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')  # zoom out 0.8X from default "normal size"
time.sleep(2.5)  # wait 2.5 seconds
driver.get("https://qasvus.wordpress.com/")  # go to : https://qasvus.wordpress.com
time.sleep(2.5)  # wait 2.5 seconds

print('Printing \'link(href)\' for header message  "California Real Estate":')
print(driver.find_element
      (By.LINK_TEXT, "California Real Estate").get_attribute(
    "href"))  # print link(href) for header "California Real Estate"
time.sleep(1.5)  # wait 1.5 seconds

print('Printing \'link(src)\' for first home image under  "About us":')
print(driver.find_element
      (By.XPATH, "//img[@class='wp-image-55']").get_attribute(
    "src"))  # print link(src) for first home image under "About us"
time.sleep(1.5)  # wait 1.5 seconds

print('Verifying via \'do assert\' that "California Real Estate" is in the website title')
assert "QA at Silicon Valley Rea" in driver.title  # verify (do assert) that "California Real Estate" in website title
print('Printing \'driver.title\':')
print(driver.title)

driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")  # find "Send Us a Message"
print('Verifying presence of "Send Us a Message" on webpage')
print(driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").text)  # verify presence on webpage

# Fill out and send the message form using the ID, Name, XPath, and Link_Text or Link_Partial_Text tags tags
# element = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
print('Filling out and sending the message form using the ID, Name, XPath, and Link_Text or Link_Partial_Text tags')
driver.implicitly_wait(5)
driver.find_element(By.NAME, "g2-name").send_keys("Yuri")
driver.find_element(By.ID, "g2-email").send_keys("yuri_dk@yahoo.com")
driver.find_element(By.XPATH, "//textarea[@class='textarea']").send_keys("Greetings!!!")
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").location_once_scrolled_into_view
driver.implicitly_wait(10)
time.sleep(2.5)
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").submit()
time.sleep(2.5)

print('Finding "go back" link and clicking it go back to the Main page')
driver.find_element(By.LINK_TEXT, "go back").location_once_scrolled_into_view
print(driver.find_element(By.LINK_TEXT, "go back").get_attribute("href"))  # find "go back" link
time.sleep(1.5)  # wait 1.5 seconds
print('I was able to locate "go back"')
driver.find_element(By.LINK_TEXT, "go back").send_keys('\n')  # click "go back" link to go back to the Main page
print('Verifying Main page by finding and printing "type" for "Submit" button:')
print('type:',
      driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))  # find and print
# "type" for "Submit" button
# to verify Main page
print('text:',
      driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").text)  # print text for "Submit" button
time.sleep(2.5)  # wait 2.5 seconds
driver.close()  # close browser tab
