from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
driver.get("http://www.yahoo.com")
sleep(5)
driver.find_element_by_xpath("//input[@name='p']").send_keys("python")
driver.find_element_by_xpath('//div[@class="mag-glass"]').click()


