"""
SeleniumWebdriver tasks:
1. Create Unit tests automation framework for our test website
2. Go to : https://qasvus.wordpress.com/
3. First Unit test for Chrome browser:
- for maximized window
- and for 1120x550 pixels
4. Second Unit test for Firefox browser:
- for maximized window
- and for 1250x850 pixels
5. Maximize window for Chrome on start of your test and use window by default for Firefox
6. Set waiting time after get.url()
- 3 seconds for Chrome
- 5 seconds for Firefox
7. Set wait.until() for Submit button in Chrome using "XPath"
8. Set wait.until() for "textarea" field in Firefox using "id"
9. Do assertions for driver title
10. Print driver title with custom explanation string
11. Clear fields: text area, first and last name
12. Fill out all fields and click on Submit button
13. Use "try/except" method to wait until "go back" link is VISIBLE and click it after
14. Use "wait.until" method for visibility of all 4 houses images on the main page
15. Do assertion for page title and print it with custom string
"""

# prepare a set of test cases for features active in the Web application
# (e.g., acceptance criteria or functional testing)

# specify automation framework for test management capabilities
# (e.g., creating data-driven tests, setting up test preconditions and postconditions,
# checking the expected and actual outputs, and providing report generation capability)


import unittest  # for tests of features unavailable in webdriver
import time  # for exact browser pause via time.sleep(...)
from selenium import webdriver  # import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException


# import HtmlTestRunner

# Unit test for Chrome browser
class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_chrome_for_maximized_window(self):
        driver_ = self.driver
        driver_.get("https://qasvus.wordpress.com")  # go to: https://qasvus.wordpress.com/
        time.sleep(1.5)  # pause 1.5 seconds
        driver_.maximize_window()  # maximize window
        wait = WebDriverWait(driver_, 3)  # wait 3 seconds after get.url()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='pushbutton-wide']")))  # wait.until() for Submit button
        # using "XPath"
        time.sleep(1.5)

        assert "California Real Estate" in driver_.title  # assertions for driver title
        print("Page qasvus.wordpress.com title in Chrome is:",
              driver_.title)  # print driver title with custom explanation string
        time.sleep(1.5)

        search_name = driver_.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Arthur Ne")
        time.sleep(1.5)  # pause 1.5 seconds
        search_email = driver_.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("arthur.nech@gmail.com")
        time.sleep(1.5)  # pause 1.5 seconds
        search_message = driver_.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        time.sleep(1.5)  # pause 1.5 seconds
        search_message.send_keys(
            "Test in progress")
        driver_.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_.implicitly_wait(4.5)

        try:
            wait.until(
                (EC.visibility_of_element_located(
                    (By.XPATH, "//a[contains(text(),'go back')]"))))  # wait till "go back" link is VISIBLE
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")  # warn that "go back" link is INVISIBLE
            time.sleep(2.5)  # pause 2 seconds

        driver_.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()  # click on "go back" link
        driver_.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-55']")))  # wait till 1st house images is VISIBLE
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-34']")))  # wait till 2nd house images is VISIBLE
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-56']")))  # wait till 3rd house images is VISIBLE
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//img[@class='wp-image-30']")))  # wait till 4th house images is VISIBLE

        driver_.implicitly_wait(4)

        assert "California Real Estate" in driver_.title
        print("After clicking 'Go back' button we're back to the right page:", driver_.title)
        time.sleep(1)  # pause 1 second

    def test_chrome_for_1120x550_pixels(self):
        driver_ = self.driver
        driver_.set_window_size(1120, 550)
        driver_.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver_, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)  # pause 1 second

        assert "California Real Estate" in driver_.title
        print("Page title in Chrome is:", driver_.title)
        time.sleep(1.5)  # pause 1 second

        # clear fields: text area, first and last name
        search_name = driver_.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_email = driver_.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_message = driver_.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        wait = WebDriverWait(driver_, 3)

        # fill out all fields and click on 'Submit' button
        driver_.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Yuri Levchuk")
        time.sleep(1.5)  # pause 1.5 seconds
        driver_.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("yuri.levchuk.dk@gmail.com")
        time.sleep(1.5)  # pause 1.5 seconds
        driver_.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "Test in progress")
        time.sleep(1.5)  # pause 1.5 seconds
        driver_.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_.implicitly_wait(4.5)  # wait 4 seconds

        html = driver_.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)

        try:
            wait.until(
                (EC.visibility_of_element_located(
                    (By.XPATH, "//a[contains(text(),'go back')]"))))  # wait till "go back" link is VISIBLE
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2.5)

        driver_.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))  # wait till 1st house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))  # wait till 2nd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))  # wait till 3rd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))  # wait till 4th house images is VISIBLE
        driver_.implicitly_wait(4)

        assert "California Real Estate" in driver_.title
        print("Page title in Chrome is:", driver_.title)
        time.sleep(1.5)

        assert "California Real Estate" in driver_.title
        print("After clicking 'Go back' button we're back to the right page:", driver_.title)
        time.sleep(1.5)

    def tearDown(self):
        self.driver.quit()


class FireFoxTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fire_fox(self):
        driver_ = self.driver
        driver_.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver_, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1.5)

        assert "California Real Estate" in driver_.title
        print("Page title in Chrome is:", driver_.title)
        time.sleep(1.5)

        # fill out all fields and click on 'Submit' button
        search_name = driver_.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Arthur Ne")
        time.sleep(1.5)  # pause 1.5 seconds
        search_email = driver_.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("arthur.nech@gmail.com")
        time.sleep(1.5)  # pause 1.5 seconds
        search_message = driver_.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        time.sleep(1.5)  # pause 1.5 seconds
        search_message.send_keys(
            "Test in progress")
        driver_.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_.implicitly_wait(4.5)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2.5)

        driver_.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))  # wait till 1st house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))  # wait till 2nd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))  # wait till 3rd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))  # wait till 4th house images is VISIBLE

        assert "California Real Estate" in driver_.title
        print("After clicking 'Go back' button we're back to the right page:", driver_.title)
        time.sleep(1.5)

    def test_fire_fox_default_1250x850_window(self):
        driver_ = self.driver
        driver_.get("https://qasvus.wordpress.com")
        driver_.set_window_size(1250, 850)
        wait = WebDriverWait(driver_, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1.5)

        assert "California Real Estate" in driver_.title
        print("Page title in Chrome is:", driver_.title)
        time.sleep(1.5)

        search_name = driver_.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Arthur Ne")
        time.sleep(1.5)  # pause 1.5 seconds
        search_email = driver_.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("arthur.nech@gmail.com")
        time.sleep(1.5)  # pause 1.5 seconds
        search_message = driver_.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "Test in progress")
        time.sleep(1.5)  # pause 1.5 seconds
        driver_.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_.implicitly_wait(4.5)

        html = driver_.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2.5)

        driver_.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))  # wait till 1st house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))  # wait till 2nd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))  # wait till 3rd house images is VISIBLE
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))  # wait till 4th house images is VISIBLE

        assert "California Real Estate" in driver_.title
        print("After clicking 'Go back' button we're back to the right page:", driver_.title)
        time.sleep(1.5)

    def tearDown(self):
        self.driver.quit()
