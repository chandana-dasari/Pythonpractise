from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver=webdriver.Chrome("./chromedriver")
driver.get("file:///C:/Users/Jagadeesh/Desktop/Selenium_Training/Training/html%20files/loading.html")
sleep(5)
w=WebDriverWait(driver,timeout=10)
#v=visibility_of_element_located(("xpath","//input[@name='fname']"))
v=visibility_of_element_located(("name","fname"))
w.until(v)
print("Firstname is visible & edited")
#sleep(3)
driver.find_element_by_name('fname').send_keys("good")
#sleep(3)

driver.find_element('name','lname').send_keys("morning")
driver.find_element('name','login').click()
