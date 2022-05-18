from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
driver.get("https://in.yahoo.com/")
sleep(5)
search_bar=driver.find_element_by_xpath("//input[@id='yschsp']").send_keys("Electronic gadgets")
sleep(2)
#search_bar.click()
driver.find_element_by_xpath("//div[@class='mag-glass']").click()
sleep(3)
driver.find_element_by_xpath("//li[@class='fl-l']").click()
sleep(5)