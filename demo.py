from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
driver.get("file:///C:/Users/Jagadeesh/Desktop/Selenium_Training/Training/html%20files/sample.html")
sleep(5)
#driver.close()
#driver.find_element_by_xpath("//div[@class='A8SBwf']").send_keys("Python")
#sleep(5)
#browser_title=driver.title
#print(browser_title)
#url=driver.current_url
#print(url)
driver.find_element_by_xpath("//input[@type='text']").send_keys("chandana")
sleep(2)
#driver.find_element_by_xpath("//option[text()='Yahoo']").click()
#sleep(2)
driver.find_element_by_xpath("//a[text()='Google']").click()
sleep(2)
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("Python")
sleep(2)
driver.find_element_by_xpath("//span[text()='python']").click()
sleep(2)
driver.find_element_by_xpath("//h3[text()='Welcome to Python.org']").click()
sleep(2)
driver.find_element_by_xpath("//a[text()='Downloads']").click()
sleep(2)
python=driver.find_element_by_xpath("//a[text()='Python 3.9.6']/../..//a[text()='Release Notes']").click()
#print(python.text)
driver.find_element_by_xpath("//input[@value='Search']").send_keys("hello")
sleep(2)
driver.find_element_by_xpath("//input[@value='Go']").click()
sleep(3)


