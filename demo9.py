from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located,title_contains
driver=webdriver.Chrome("./chromedriver")
driver.get("file:///C:/Users/Jagadeesh/Desktop/Selenium_Training/Training/html%20files/progressbar.html")
sleep(5)
driver.find_element_by_xpath("//button[text()='Click Me']").click()
w=WebDriverWait(driver,10)
v=visibility_of_element_located(("xpath","//div[text()='100%']"))
w.until(v)
print("DONE!!!")
w=WebDriverWait(driver,10)
v=title_contains("DemoWebShop")
w.until(v)
#sleep(2)
