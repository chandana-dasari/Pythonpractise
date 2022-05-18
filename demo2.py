from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
#driver.get("https://www.python.org/")
#sleep(5)
driver.get("file:///C:/Users/Jagadeesh/Desktop/Selenium_Training/Training/html%20files/css_selector.html")
sleep(4)
#driver.find_element_by_xpath("//h1[@class='site-headline']/../..//img[@class='python-logo']")
#sleep(5)
#Example for Relative xpath
driver.find_element_by_xpath("//input[@type='text']").send_keys("chandu")
sleep(4)
driver.find_element_by_xpath("//input[@type='password']").send_keys("chandu")
sleep(2)
