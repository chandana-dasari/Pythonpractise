from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
driver.get("http://www.zohocrm.com")
#driver.find_element_by_xpath("(//a[@class='zgh-login'])[1]").click()
#driver.find_element_by_xpath("//input[@id='login_id']").send_keys("dasarichandana111@gmail.com")
#driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_xpath("//a[text()='All Products']").click()
driver.find_element_by_xpath("//a[@class='zgh-i-forms']/../../..").click()





#sleep(2)

