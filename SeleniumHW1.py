from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element(By.XPATH, "//p[@class='site-title']//a[contains(text(), 'California Real Estate')][@rel='home']").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55']").get_attribute("src"))
assert "California Real Estate" in driver.title

print(driver.title)
element = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
driver.implicitly_wait(5)
driver.find_element(By.ID, "g2-name").send_keys("Alex")
driver.find_element(By.ID, "g2-email").send_keys("actum21@gmail.com")
driver.find_element(By.XPATH, "//textarea[@class='textarea']").send_keys("Hello!!!")

# Начиная от сюда не работает и не могу дальше проверить.
btnClick = driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']")

# //main[@id='main']//div[@id='contact-form-2']//a[@href='/?contact-form-hash=ba2938b804d2758df7e6353f6769437bbd9049a3']

btnClick.submit()
driver.implicitly_wait(10)

btnGoB = driver.find_element(By.XPATH, "//a[contains(text(),'go back')]")
btnGoB.click()

# driver.find_element(By.XPATH, "//*[@xpath='1']").click()
driver.find_element(By.CLASS_NAME, "pushbutton-wide")
assert "Submit" in driver.page_source


driver.quit();